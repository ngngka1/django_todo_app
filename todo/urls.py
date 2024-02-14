from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home_page),
    path('createtodos/', views.create_todo),
    path('modifytodos/', views.modify_todos),
    path('deletetodos/', views.delete_todos),
]