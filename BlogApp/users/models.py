from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 250)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

##Without the __str__ itll only print out the profile object
    def __str__(self):
        return f'{self.user.username} Profile'
