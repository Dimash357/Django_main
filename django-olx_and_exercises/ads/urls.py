from django.urls import path
from . import views

urlpatterns = [
    path('ad_list/', views.ad_list, name='ad_list'),
    path('ad_create/', views.ad_create, name='ad_create'),
]