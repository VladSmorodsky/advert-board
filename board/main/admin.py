from django.contrib import admin

from main.models import User, Advert, Category, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Advert)
admin.site.register(Category)
admin.site.register(Comment)
