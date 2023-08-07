from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    mentioned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentioned_in_posts', blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, default=None)
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    downvote = models.BooleanField(default=False)


