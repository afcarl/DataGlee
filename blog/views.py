from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.utils import timezone
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
import blog.trial
import blog.playlist
import collections
from django import forms

# from blog.playlist import playlist_id

def homepage(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/homepage.html',{'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def yelping(request):
	return render(request, 'blog/yelping.html')

def IndianRailways(request):
	return render(request, 'blog/IndianRailways.html')

def Gapminder(request):
	return render(request, 'blog/Gapminder.html')	
	
def Youtube(request):
	if request.method == 'POST':
		a = request.POST.get("title", "")
		s = blog.trial.start(a)
		a = s[0]
		post1 = blog.playlist.playlist_id()
		#Do your stuff ,calling whatever you want from set_gpio.py
		return render(request, 'blog/Youtube.html',{'post1':post1[0],'s':s[1:],'a':a})		
	else:
		post1 = blog.playlist.playlist_id()
		return render(request, 'blog/Youtube.html',{'post1': post1[0]})




	