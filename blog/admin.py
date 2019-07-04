from django.contrib import admin
from .models import Article,Author,Tag
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','score',)
    ordering = ['score']#排序
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','qq','email',)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
# Register your models here.
