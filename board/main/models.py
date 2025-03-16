from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class User(AbstractUser):
    password = models.CharField(max_length=128, verbose_name="password")
    phone = models.CharField(max_length=15, unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="User_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="User_set")

    def __str__(self) -> str:
        return f"{self.username}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_active_adverts_count(self) -> int:
        """
        Show active adverts count for this category.
        :return:
        """
        return self.adverts.filter(is_active=True).count()


class Advert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, models.DO_NOTHING, related_name="adverts")

    def get_short_description(self) -> str:
        """
        Show short description for this advert.
        :return:
        """
        return f"{self.description}"[:101]

    def get_comments_count(self) -> int:
        """
        Show comments count for this advert.
        :return:
        """
        return self.comments.count()

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.advert.title}: created at {self.created_at}"
