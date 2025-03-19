from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from main.models import User, Advert, Category, Comment


class AdvertAdmin(admin.ModelAdmin):
    list_filter = ['category__name', 'is_active', 'price', 'created_at']
    search_fields = ['title']
    sortable_by = ['created_at', 'price']


# Register your models here.
admin.site.register(User)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Category)
admin.site.register(Comment)
