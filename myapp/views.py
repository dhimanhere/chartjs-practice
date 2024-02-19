from django.shortcuts import render, redirect
from .models import myModel
import json
from datetime import datetime
from django.db.models import Count,Avg
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.forms import InsightForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

    data = myModel.objects.all().order_by("pk")
    paginate = Paginator(data, 10)
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

def detailview(request, pk):
    post = get_object_or_404(myModel, pk=pk)

    previous_post = myModel.objects.filter(pk__lt=post.pk).order_by('-pk').first()

    next_post = myModel.objects.filter(pk__gt=post.pk).order_by('pk').first()
    context = {
        'post':post,
        'previous_post_url': reverse('detail', args=[previous_post.pk]) if previous_post else None,
        'next_post_url': reverse('detail', args=[next_post.pk]) if next_post else None,
    }
    return render(request, 'myapp/detail.html', context)

def logview(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect("/")
            else:
                messages.error(request, "Username and Password does not match")
        return render(request, 'myapp/login.html')

def lg(request):
    logout(request)
    return redirect("/")

@login_required(login_url = "/login/")
def modelform(request):
    if request.method == "POST":
        form = InsightForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Oops! Something went wrong")
    else:
        form = InsightForm()
    context = {
        'form':form,
    }
    return render(request, "myapp/form.html", context)