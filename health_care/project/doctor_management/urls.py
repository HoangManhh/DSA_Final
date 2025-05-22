from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/update/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),
]