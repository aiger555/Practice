from django.db import models



class Page(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

