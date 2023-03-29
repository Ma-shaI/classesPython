from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def home(request):
    datas = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'datas': datas})


def about(request):
    return render(request, 'portfolio/about.html')


def works(request):
    datas = Portfolio.objects.all()
    return render(request, 'portfolio/work.html', {'datas': datas})


def contact(request):
    return render(request, 'portfolio/contact.html', {'flag': True})
