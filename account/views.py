from django.shortcuts import render
from django.urls import reverse_lazy 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from .forms import SignUpForm
from post.models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


class SignUpView(CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

	

class PostListView(ListView):
	context_object_name = 'post_list'
	template_name ='registration/profile.html'

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(PostListView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)



class PostCreateView(CreateView):
	model = Post
	fields = [
		'title',
		'slug',
		'content',
	]
	template_name = 'create_post.html' # Template revie

	#Save Login user To 
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView,self).form_valid(form)

	#Redirect after success
	def get_success_url(self):
		return reverse_lazy('profile')

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(PostCreateView, self).dispatch(*args, **kwargs)

	

class PostUpdateView(UpdateView):
	model = Post
	fields = [
		'title',
		'slug',
		'content',
	]
	template_name = 'update_post.html'

	def get_success_url(self):
		return reverse_lazy('profile')

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(PostUpdateView, self).dispatch(*args, **kwargs)



class PostDeleteView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('profile')

	def get_success_url(self):
		return reverse_lazy('profile')

	@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(PostDeleteView, self).dispatch(*args, **kwargs)


	
