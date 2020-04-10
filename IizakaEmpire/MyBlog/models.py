from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=16)
    slug=models.SlugField(max_length=8,unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=16)
    slug=models.SlugField(max_length=8,unique=True)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    slug=models.SlugField(max_length=16,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)
    title=models.CharField(max_length=64)
    meta_description=models.CharField(max_length=64)
    ogp_title=models.CharField(max_length=32)
    ogp_img=models.ImageField(upload_to='ogp_img')
    pub_date=models.DateTimeField('作成日時',auto_now_add=True)
    up_date=models.DateTimeField('更新日時',auto_now=True)
    contents=MarkdownxField('Contents',help_text='To Put Artile')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-pub_date']

    def exchange_markdown(self):
        return markdownify(self.contents)

class Author(models.Model):
    profimg=models.ImageField(upload_to='author/')
    name=models.CharField(max_length=16)
    contents=MarkdownxField('Contents',help_text='To Put your profile')

    def __str__(self):
        return self.name
    
    def exchange_markdown(self):
        return markdownify(self.contents)