from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


MAX_PAGE = 10


def home(request, page=1):
    start = MAX_PAGE * (page-1)
    end = MAX_PAGE * page
    posts = Post.objects.filter(post_date__lte=timezone.now())[start:end]
    
    return render(request, 'blog/home.html', {'posts': posts})


def post(request, post_id, slug):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post': post})