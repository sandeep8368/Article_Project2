from django.contrib import admin
from myapp.models import ArticleModel
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
    
admin.site.register(ArticleModel, ArticleAdmin)