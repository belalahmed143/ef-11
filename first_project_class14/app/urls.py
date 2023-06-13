from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('banner_add', banner_add, name='banner_add'),
    path('banner_detail/<title>', banner_detail, name='banner_detail'),
    path('banner_edit/<pk>', banner_edit, name='banner_edit'),
    path('banner_delete/<pk>', banner_delete, name='banner_delete'),

]