from django.db import models
from django.utils import timezone
from users.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.author}"
    
class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message} | {self.post.title} | {self.author.username}"