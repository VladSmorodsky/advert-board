from django.contrib import admin

from main.models import User, Advert, Category, Comment


class AdvertAdmin(admin.ModelAdmin):
    list_filter = ['category__name', 'is_active']


# Register your models here.
admin.site.register(User)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Category)
admin.site.register(Comment)
