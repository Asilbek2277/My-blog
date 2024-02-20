from django.contrib import admin

from .models import *
admin.site.register(Article)
admin.site.register(ArticleItems)
admin.site.register(SocialMedia)

