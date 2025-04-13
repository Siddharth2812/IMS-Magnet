from django.urls import path
from . import views

urlpatterns = [
    path('api/suppliers/', views.supplier_list, name='supplier-list'),
    path('api/suppliers/<int:pk>/', views.supplier_detail, name='supplier-detail'),
] 