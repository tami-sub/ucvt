from django.contrib import admin
from project.models import Partner, Message, Customer

# Register your models here.
# class ArticleInline(admin.StackedInline):
#     model = Comments
#     extra=2

# class ArticleAdmin(admin.ModelAdmin):
#     fields = ['article_table', 'article_test', 'article_date']
#     inlines = [ArticleInline]
#     list_filter = ['article_date']

# admin.site.register(Article, ArticleAdmin)

# class CustomerAdmin(admin.ModelAdmin):
#     title = 'country'
#     fields = ['__all__']
#     parameter_name = 'country'


admin.site.register(Partner)
admin.site.register(Message)
admin.site.register(Customer)