from django.db import models
from django.utils import timezone
from django.urls import reverse
from colorfield.fields import ColorField
from django.conf import settings
from os.path import join



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(default=join(settings.STATIC_URL, "images/logo.jpeg"), blank=False, upload_to="article_images" )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Tag(models.Model):
    post = models.ManyToManyField(Post, related_name='tags')
    name = models.CharField(max_length=50)
    color = ColorField(default="FF0000", blank=False)



