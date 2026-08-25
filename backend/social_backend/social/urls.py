from django.urls import path
from . import views

urlpatterns = [
    path('api/feed/', views.feed),
    path('api/create_post/', views.create_post),
    path('api/add_comment/', views.add_comment),
    path('api/toggle_follow/', views.toggle_follow),
    path('api/like/<int:post_id>/', views.like_post),
]