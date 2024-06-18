from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def index(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'blog/post.html', context={'page_obj': page_obj, 'posts': page_obj.object_list})

def about(request):
    return render(request, 'blog/about.html')
