from django.urls import path
from main import views


urlpatterns = [
    path('', views.redirect_home_page, name='redirect_home_page'),
    path('home/', views.home_page, name='home_page'),
]