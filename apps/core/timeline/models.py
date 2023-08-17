from django.db import models
from apps.core.seats.models import StaffSeat

class Post(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)
class Comment(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
