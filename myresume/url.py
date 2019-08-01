from django.urls import path

from . import views

urlpatterns = [
#     path('', views.index, name='index'),
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]