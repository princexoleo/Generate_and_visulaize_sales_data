import uuid, base64
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

# Generate transaction id
def generate_code():
    return str(uuid.uuid4()).replace("-", "").upper()[:12]

def get_salesman_from_id(val):
    return Profile.objects.get(id=val).user.username

def get_customer_from_id(val):
    return Customer.objects.get(id=val)


# Generate graph
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_key(res_by):
    if res_by == '#1':
        return 'transaction_id'
    elif res_by == '#2':
        return 'created_at'


def get_chart(chart_type, data, result_by, **kwargs):
    plt.switch_backend('agg')
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5))
    key = get_key(result_by)
    d = data.groupby(key, as_index=False)['total_price'].agg('sum')
    # now check the condition
    if chart_type == '#1':
        #plt.bar(d[key], d['total_price'] , color='#0066ff', width=0.5)
        sns.barplot(data=d, x=key, y='total_price')
    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data=d, x="total_price", labels=d[key].values, autopct='%1.1f%%')
    elif chart_type == '#3':
        plt.plot(d[key], d['total_price'], color='#0066ff', marker='o')
    else:
        print('..Failed to identify the chart type....')
    plt.tight_layout()
    chart = get_graph()
    return chart

