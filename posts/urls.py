from django.urls import path
from . import views


urlpatterns =[
    path('', views.index),
    path('post/<str:pk>/', views.post),
]