from django.shortcuts import render
from .models import myModel
import json
from datetime import datetime
from django.db.models import Count,Avg
from django.core.paginator import Paginator

def home(request):

    c_c = myModel.objects.values('country').annotate(c=Count('country'))
    
    c_r = myModel.objects.values('country').annotate(
        avr=Avg('relevance'),
        con=Count('country')
        )

    c_i = myModel.objects.values('country').annotate(
        c=Count('country'),
        avr=Avg('intensity')
        )

    c_l = myModel.objects.values('country').annotate(
        c=Count('country'),
        avr=Avg('likelihood')
        )

    data = myModel.objects.all().order_by("?")
    paginate = Paginator(data, 20)
    page_number = request.GET.get("page")
    page_list = paginate.get_page(page_number)
    context={
        "c_c":c_c,
        "c_r":c_r,
        "c_i":c_i,
        "c_l":c_l,
        "page_list":page_list,
    }
    return render(request, 'myapp/home.html', context)