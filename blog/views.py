from django.shortcuts import render


def index(request):
    return render(request, 'blog/post.html')


def about(request):
    return render(request, 'blog/about.html')
