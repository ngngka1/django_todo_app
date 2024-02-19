from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_home_page),
    path('get/', views.get_data),
    path('get/<str:pk>/', views.get_data),
    path('add/', views.add_data),
    path('modify/<str:pk>/', views.modify_data), # pk: primary key
    path('delete/<str:pk>/', views.delete_data),
]