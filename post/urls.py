from django.urls import path 
from .views import PostListView, PostDetailView


urlpatterns = [
     path('',PostListView.as_view(), name="index"),
     path('<slug:slug>/',PostDetailView.as_view(),name="details_post")
] 