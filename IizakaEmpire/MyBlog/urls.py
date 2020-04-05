from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<int:blog_id>/',views.blog,name='blog'),
    path('markdownx/',include('markdownx.urls')),
]