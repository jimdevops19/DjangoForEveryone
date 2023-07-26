from django.urls import path
from main import views


urlpatterns = [
    # path('', views.redirect_login_page, name='redirect_login_page'),
    path('/home', views.redirect_home_page, name='redirect_home_page'),
    
    path('home/', views.home_page, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('item/', views.item_page, name='item_page'),
    path('employeelist/', views.employee_page, name='item_page')
    
]