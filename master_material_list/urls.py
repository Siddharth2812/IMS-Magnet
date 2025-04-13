from django.urls import path
from . import views

urlpatterns = [
    path('api/materials/', views.material_list, name='material-list'),
    path('api/materials/<int:pk>/', views.material_detail, name='material-detail'),
] 