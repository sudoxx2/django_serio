from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Nani',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'omerae',
        'title': 'blog post 2',
        'content': 'First post content',
        'date_posted': 'July 27, 2018'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})