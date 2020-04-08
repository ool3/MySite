from django.contrib import admin
from .models import Article,Category,Tag
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Article,MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)