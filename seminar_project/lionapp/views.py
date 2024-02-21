from django.shortcuts import get_object_or_404, render

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from lionapp.models import *

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = {
        'id': post.pk,
        '제목': post.title,
        '내용': post.content,
        '메시지': '조회 성공'
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})