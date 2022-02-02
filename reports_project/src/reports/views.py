from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from .models import Report
from sales.models import Sale, Position, CSV
from products.models import Product
from customers.models import Customer
from django.http import JsonResponse,HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.dateparse import parse_date
import datetime as dt
import os
import csv
import pandas as pd
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# import timezone from django
from django.utils import timezone
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .utils import get_report_image
from .forms import ReportForm

# Create your views here.
class ReportListView(LoginRequiredMixin,ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'


class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = 'reports/report_detail.html'
    context_object_name = 'report'


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# def create_report_view(request):
#     form = ReportForm(request.POST or None)
#     print(request.user)
#     if is_ajax(request):
#         # name = request.POST.get('name')
#         # remarks = request.POST.get('remarks')
#         # image = request.POST.get('image')

#         img = get_report_image(image)
#         author = Profile.objects.get(user=request.user)
#         #print(image, img, author)
#         Report.objects.create(name=name, remarks=remarks, image=img, author=author)

#         # if form.is_valid():
#         #     instance = form.save(commit=False)
#         #     instance.image = img
#         #     instance.author = author
#         #     instance.save()

#         return JsonResponse({'msg': 'send'})
#     return JsonResponse({})
@login_required
def create_report_view(request):
    form = ReportForm(request.POST or None)
    print(request.user)
    if is_ajax(request):
        image = request.POST.get('image')
        img = get_report_image(image)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = Profile.objects.get(user=request.user)
            instance.save()
        return JsonResponse({'msg': 'send'})
        
    return JsonResponse({})

class UploadTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "reports/upload_file.html"


@login_required
def csv_upload_view(request):
    print('file is being')

    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    data = ",".join(row)
                    data = data.split(',')
                    #data.pop()
        
                    transaction_id = data[1]
                    product = data[2]
                    quantity = int(data[3])
                    customer = data[4]
                    date = dt.datetime.strptime(data[5], "%d/%m/%Y").date()

                    try:
                        product_obj = Product.objects.get(name__iexact=product)
                    except Product.DoesNotExist:
                        product_obj = None

                    if product_obj is not None:
                        customer_obj, _ = Customer.objects.get_or_create(name=customer) 
                        salesman_obj = Profile.objects.get(user=request.user)
                        position_obj = Position.objects.create(product=product_obj, quantity=quantity, created_at=date,updated_at=timezone.now())

                        sale_obj, _ = Sale.objects.get_or_create(transaction_id=transaction_id, customer=customer_obj, salesman=salesman_obj, created_at=date)
                        sale_obj.positions.add(position_obj)
                        sale_obj.save()
                return JsonResponse({'msg': False})
        else:
            return JsonResponse({'msg': True})

    return HttpResponse()


#
@login_required
def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report, pk=pk)
    context = {'obj': obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if we want to display the pdf in browser
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response