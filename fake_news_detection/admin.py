from django.contrib import admin

from fake_news_detection.models import NewsArticle


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('newspaper', 'category', 'news_text', 'label')


# Register your models here.
admin.site.register(NewsArticle, NewsArticleAdmin)