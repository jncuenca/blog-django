from django.urls import path
from .views import index, get_post_view, create_post_view, delete_post

app_name = 'posts'
urlpatterns =[
    path('', index, name='index'),
    path('create-post/', create_post_view, name='create-post'),
    path('get-post/<str:pk>/', get_post_view, name='get-post'),
    path('delete-post', delete_post, name='delete-post'),
]