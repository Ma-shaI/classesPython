from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name
