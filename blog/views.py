from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def homepage(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/homepage.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def yelping(request):
	return render(request, 'blog/yelping.html')
