from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
	paginate_by = 5
	queryset = Post.objects.filter(status=1)
	template_name ='index.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'details_post.html'


