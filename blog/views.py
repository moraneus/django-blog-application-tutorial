from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Post
import json


@require_GET
def post_list(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'query': query})


@require_GET
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


@csrf_exempt
@require_POST
def create_post(request):
    if request.content_type == 'application/json':
        data = json.loads(request.body)
        post = Post.objects.create(title=data['title'], content=data['content'])
        return JsonResponse(
            {'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at})
    else:
        # Handle form submission
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('post_list')


@csrf_exempt
@require_http_methods(["PUT"])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = json.loads(request.body)
    post.title = data['title']
    post.content = data['content']
    post.save()
    return JsonResponse({'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return JsonResponse({'message': 'Post deleted'})


@csrf_protect
@require_http_methods(["POST"])
def update_post_form(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('post_list')


@csrf_protect
@require_GET
def create_post_form(request):
    return render(request, 'blog/create_post.html')


@csrf_protect
@require_GET
def update_post_form_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/update_post.html', {'post': post})
