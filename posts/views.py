from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if title == "" or body == "":
            return render(request, 'index.html', {'posts':Post.objects.all(), 'message': 'Empty field/s. Post not added'})

        post = Post.objects.create(title= title, body=body)
        post.save()


    
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post.html", {"post":post})

