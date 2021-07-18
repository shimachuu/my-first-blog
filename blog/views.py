from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #リクエストというのは、インターネットを介してユーザから受け取った全ての情報が詰まったものです
    return render(request, 'blog/post_list.html', {'posts':posts})

