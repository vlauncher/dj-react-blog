from django.db import models
from users.models import User

# Create your models here.

class Posts(models.Model):
    topic = models.CharField('Topic',max_length=100)
    message = models.CharField('Message',max_length=300)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owners_post')