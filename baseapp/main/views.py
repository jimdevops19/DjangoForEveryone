from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from stock.models import Item
from .models import employee
from main import views
# Create your views here.
def redirect_home_page(request):
    return redirect('home_page')
def redirect_login_page(request):
    return redirect('login_page')
def redirect_itemlist_page(request):
    return redirect('item_page')
def redirect_employeelist_page(request):
    return redirect('employee_page')


def home_page(request):
    # item=Item.objects.all()
    # context={'item': item}
    # return render(request,'main/home.html', context)
    return render(
        request,
        template_name='main/home.html',
        context={}
    )

def login_page(request):
    return render(
        request,
        template_name='main/login.html',
        context={}
    )
def item_page(request):

    item=Item.objects.all()
    context={'item':item}
    return render(
        request,
        'main/item.html', context
    )
def employee_page(request):

    employees=employee.objects.all()
    context={'employee':employees}
    return render(
        request,
        'main/employeeList.html', context
    )