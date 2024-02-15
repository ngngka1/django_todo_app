from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home_page, name="todo-home"),
    path('create-todo/', views.create_todo, name="create-todo"),
    path('modify-todo/<str:pk>/', views.modify_todo, name="modify-todo"),
    path('delete-todo/<str:pk>/', views.delete_todo, name="delete-todo"),
]