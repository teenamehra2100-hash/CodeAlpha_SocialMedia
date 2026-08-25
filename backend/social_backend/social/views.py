from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post, Comment, Follow, Like
import json


def cors_response(data, status=200):
    response = JsonResponse(data, safe=False, status=status)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    return response


def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    data = []
    for p in posts:
        data.append({
            'id': p.id,
            'username': p.user.username,
            'content': p.content,
            'created_at': p.created_at.strftime("%b %d, %Y, %I:%M %p"),
            'likes': p.likes.count(),
            'comments': [{'username': c.user.username, 'content': c.content} for c in p.comments.all()]
        })
    return cors_response(data)


@csrf_exempt
def create_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        content = data.get("content")
        user, created = User.objects.get_or_create(username=username)
        post = Post.objects.create(user=user, content=content)
        return cors_response({'message': 'Post created', 'id': post.id}, status=201)
    return cors_response({'error': 'POST only'}, status=405)


@csrf_exempt
def add_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        post_id = data.get("post_id")
        content = data.get("content")
        user, created = User.objects.get_or_create(username=username)
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, user=user, content=content)
        return cors_response({'message': 'Comment added', 'id': comment.id}, status=201)
    return cors_response({'error': 'POST only'}, status=405)


@csrf_exempt
def toggle_follow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        follower_username = data.get("follower_username")
        following_username = data.get("following_username")
        follower, _ = User.objects.get_or_create(username=follower_username)
        following, _ = User.objects.get_or_create(username=following_username)
        follow, created = Follow.objects.get_or_create(follower=follower, following=following)
        if not created:
            follow.delete()
            return cors_response({'following': False})
        return cors_response({'following': True})
    return cors_response({'error': 'POST only'}, status=405)


@csrf_exempt
def like_post(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        user, _ = User.objects.get_or_create(username=username)
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            like.delete()
        return cors_response({'likes': post.likes.count()})
    return cors_response({'error': 'POST only'}, status=405)