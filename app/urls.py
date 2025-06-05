from django.urls import path
from . import views

urlpatterns = [
    path('', views.mcq_list, name='mcq_list'),
    path('add/', views.add_mcq, name='add_mcq'),
]