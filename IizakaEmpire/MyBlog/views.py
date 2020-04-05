from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):

    putart=Article.objects.all()

    contents={
        'article':putart,
    }

    return render(request,'index.html',contents)

def blog(request,blog_id):

    putart=Article.objects.get(id=blog_id)

    contents={
        'article':putart,
    }

    return render(request,'blog.html',contents)
