from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    ##title = models.CharField(max_length = 100)
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pic = models.ImageField(default='default.jpg',upload_to ='images')
    likes = models.ManyToManyField(User,related_name ='blog_posts')
    ##likes = models.IntegerField(default = 0)
    def total_likes(self):
        return self.likes.count()
        ##return self.likes

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})
