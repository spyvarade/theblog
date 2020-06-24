from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
					SignUpView,
					PostListView,
					PostCreateView,
					PostUpdateView,
					PostDeleteView,
					)

urlpatterns = [ 
	path('signup/',SignUpView.as_view(), name="signup"),
	path('login/', auth_views.LoginView.as_view(), name="login"),
	path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
	path('profile/', PostListView.as_view(), name='profile'),
	path('post/',PostCreateView.as_view(), name="post_create"),
    path('post/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete')
]