from django.urls import path
from . import views

urlpatterns = [
    path('api/feed/', views.feed),
    path('api/create_post/', views.create_post),
]