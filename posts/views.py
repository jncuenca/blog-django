from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def get_post_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "detail.html", {"post":post})


def create_post_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        if title == "" or body == "":
            return render(request, 'create-post.html', {'invalid': True})
        else:
            post = Post.objects.create(title=title, body=body)
            post.save()
            return redirect('posts:index')
            
    return render(request, 'create-post.html')

def delete_post(request):
    id = request.POST.get('post-id')
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts:index')