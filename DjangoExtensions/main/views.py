from django.shortcuts import render, redirect

# Create your views here.
def redirect_home_page(request):
    return redirect('home_page')

def home_page(request):
    return render(
        request,
        template_name='main/home.html',
        context={}
    )