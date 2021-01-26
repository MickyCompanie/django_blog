from django.shortcuts import render
from .models import Post

# Create your views here.}

def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()[::-1], 'title': 'Home'})

def about(request):
    return HttpResponse('<h1>Blog About</h1>')