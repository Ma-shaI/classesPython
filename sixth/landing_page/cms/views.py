from django.shortcuts import render
from .models import CmsSlider
from price.models import PriceCard, PriceTable
from crm.models import Order
from crm.forms import OrderForm


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form
    }
    return render(request, 'cms/index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(
            order_name=name, order_phone=phone,
        )
        element.save()
        return render(request, 'cms/thanks.html', {'name': name})
    else:
        return render(request, 'cms/thanks.html')
