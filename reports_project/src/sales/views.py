from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Sale
from .forms import SalesSearchForm
from reports.forms import ReportForm
from .utils import get_salesman_from_id, get_customer_from_id, get_chart


import pandas as pd 

# Create your views here.

# A function based view called home_view
@login_required
def home_view(request):
    sale_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        result_by = request.POST.get('result_by')
        print(date_from, date_to, chart_type)
        # query for collect data from database
        qs = Sale.objects.filter(created_at__range=[date_from, date_to])
        if len(qs) > 0:
            # print(qs) # this will print the quesryset
            # convert the queryset to dataframe
            sale_df = pd.DataFrame(list(qs.values()))
            sale_df['customer_id'] = sale_df['customer_id'].apply(get_customer_from_id)
            sale_df['salesman_id'] = sale_df['salesman_id'].apply(get_salesman_from_id)
            sale_df['created_at'] = sale_df['created_at'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sale_df['updated_at'] = sale_df['updated_at'].apply(lambda x: x.strftime('%Y-%m-%d'))
            sale_df.rename({'customer_id': 'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1, inplace=True)
            positions_data = []
            for sale in qs:
                for position in sale.positions.all():
                    obj = {
                        'id': position.id,
                        'sales_id': position.get_sales_id(),
                        'product_id': position.product.id,
                        'product_name': position.product.name,
                        'quantity': position.quantity,
                        'price': position.price,
                        # 'created_at': position.created_at.strftime('%Y-%m-%d'),
                        # 'updated_at': position.updated_at.strftime('%Y-%m-%d'),

                    }
                    positions_data.append(obj) 
            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(sale_df, positions_df, on='sales_id')
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')
            chart = get_chart(chart_type, sale_df, result_by)
            
            sale_df = sale_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()
            #print(sale_df.head())
        else:
            no_data = 'No data found'
        
    
    context = {
       
        'search_form': search_form,
        'report_form': report_form,
        'sale_df': sale_df,
        'positions_df': positions_df,
        'merged_df': merged_df,
        'df': df,
        'chart': chart,
        'no_data': no_data,
    }
    # Render the home.html template
    return render(request, 'sales/home.html', context)

# A class based view is the alernatives of functional-based views.
# It is a good practice to use class based views instead of function based views.
# Class-based views take care of basic functionalities such as deleting an item or add an item.
# Class-based views also take care of the template rendering.
# It helps to following the DRY principal.
# Creating class for sales listview by using django generic Listview
class SaleListView(LoginRequiredMixin , ListView):
    model = Sale
    template_name = 'sales/sales_list.html'


# Creating a class for the DetailView
class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = 'sales/sale_detail.html'

