from django.db import models
from django.utils import timezone
#from .models import Post
from django.shortcuts import render
from django import forms

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title	

class CronForm(forms.Form):
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])		