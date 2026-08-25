from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post
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