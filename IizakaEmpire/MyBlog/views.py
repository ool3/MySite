from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse,Http404
from .models import Article,Author,Category
# Create your views here.

def index(request):

    article=Article.objects.all().values_list('slug','ogp_title','meta_description','ogp_img','pub_date','category')
    
    article_List=[]

    for art in article:
        tmp=Category.objects.get(id=art[5])
        tmp_tuple=(tmp.slug,tmp.name)
        article_List.append(art+tmp_tuple)

    author=Author.objects.all()

    pagenate=Paginator(article_List,5)

    if request.GET:
        p=request.GET.get('page')
        p=int(p)
    else:
        p=1

    putart=pagenate.get_page(p)
    page_num=pagenate.page_range
    
    contents={
        'author':author,
        'article':putart,
        'page_num':page_num,
        'current_page':p,
    }

    return render(request,'index.html',contents)

def blog(request,div,blog_id):
    print(div)
    putart=Article.objects.get(slug=blog_id)
    recommend=Article.objects.all().values_list('slug','ogp_title','ogp_img','category')[:4]

    recommend_List=[]

    for art in recommend:
        tmp=Category.objects.get(id=art[3])
        tmp_tuple=(tmp.slug,tmp.name)
        recommend_List.append(art+tmp_tuple)

    tags_list=putart.tags.all()
    contents={
        'article':putart,
        'recommend':recommend_List,
        'tags':tags_list,
        'category':putart.category,
    }

    return render(request,'blog.html',contents)

def Categorys(request,type,searchtype):

    if searchtype==1:
        article=Article.objects.select_related('category').filter(category__slug=type).values_list('slug','ogp_title','meta_description','ogp_img','pub_date','category')
    elif searchtype==2:
        article=Article.objects.select_related('tags').filter(tags__slug=type).values_list('slug','ogp_title','meta_description','ogp_img','pub_date','category')
    else:
        return Http404
    
    article_List=[]

    for art in article:
        tmp=Category.objects.get(id=art[5])
        tmp_tuple=(tmp.slug,tmp.name)
        article_List.append(art+tmp_tuple)

    author=Author.objects.all()

    pagenate=Paginator(article_List,5)

    if request.GET:
        p=request.GET.get('page')
        p=int(p)
    else:
        p=1

    putart=pagenate.get_page(p)
    page_num=pagenate.page_range
    
    contents={
        'author':author,
        'article':putart,
        'page_num':page_num,
        'current_page':p,
    }

    return render(request,'index.html',contents)