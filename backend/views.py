from django.shortcuts import render

# Create your views here.
from backend.models import Hostel


def index(request):
    otel = Hostel.objects.all()
    return render(request,'index.html',{'otel': otel})


def hightolowrate(request):
    sorthightolowrate = Hostel.objects.all().order_by('rank').reverse()
    return render(request,'index.html',{'otel' : sorthightolowrate})

def hightolow(request):
    sorthightolow = Hostel.objects.all().order_by('price').reverse()
    return render(request,'index.html',{'otel' : sorthightolow})


def lowtohigh(request):
    sortlowtohigh = Hostel.objects.all().order_by('price')
    return render(request,'index.html',{'otel' : sortlowtohigh})