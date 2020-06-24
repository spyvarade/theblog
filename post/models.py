from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	"""

	Creating Post Model Belog To users

	"""
	title		= models.CharField(max_length=100, unique=True)
	slug  		= models.SlugField(max_length=100, unique=True)
	content 	= models.TextField()
	author      = models.ForeignKey(
								User, 
								on_delete= models.CASCADE 
								
								)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)
	status 		= models.BooleanField(default=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	

