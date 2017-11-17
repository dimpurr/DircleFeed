from django.contrib import admin

# Register your models here.

from .models import RSSList, RSSListSource

admin.site.register(RSSList)
admin.site.register(RSSListSource)