from django.db import models
from apps.core.seats.models import StaffSeat

class Post(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active   = models.BooleanField(default=True)
    
    def __str__(self):
        return self.content
class Comment(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

class Like(models.Model):
    author = models.ForeignKey(StaffSeat, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username + " liked " + self.post.content
# add signals 