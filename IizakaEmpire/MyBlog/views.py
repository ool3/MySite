from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):

    putart=Article.objects.all().values_list('id','ogp_title','meta_description','ogp_img')[:5]

    contents={

        'article':putart,
    }

    return render(request,'index.html',contents)

def blog(request,blog_id):

    putart=Article.objects.get(id=blog_id)
    recommend=Article.objects.all().values_list('id','ogp_title','ogp_img')[:4]

    contents={
        'article':putart,
        'recommend':recommend,
    }

    return render(request,'blog.html',contents)
