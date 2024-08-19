from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from register.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    cover_image = models.ImageField(upload_to='media/files/blog_covers',blank=True, null=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True, related_name='posts', default = 1)
    content = models.TextField(max_length= 5000)
    slug = models.SlugField(unique=True)
    published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    class Meta():
        ordering = ['-published']

    def __str__(self):
        return self.title


class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments',default=1)
        body = models.TextField(max_length=300)
        created_on = models.DateTimeField(auto_now_add=True)
        updated_on = models.DateTimeField(auto_now=True)

        class Meta:
           ordering = ['created_on']

        def __str__(self):
           return 'Comment {} by {}'.format(self.body, self.user.username)
        




