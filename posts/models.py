import os
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


def trim_string(str, limit):
    result = str[:limit]
    last_space = result.rfind(' ')
    return result[:last_space]


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('name',)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(
        upload_to='images/',
        default='images/placeholder.png',
    )

    def __str__(self):
        return self.title

    def summary(self):
        result = self.content[:70]
        last_space = result.rfind(' ')
        return result[:last_space] + '...'

    def pub_date_pretty(self):
        return self.created_at.strftime('%b %e')

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
