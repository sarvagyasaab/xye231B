from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    mentioned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentioned_in_posts', blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)