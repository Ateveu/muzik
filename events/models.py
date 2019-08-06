from django.db import models


class Event(models.Model):
    arstist = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20, default="")
    genre = models.CharField(max_length=30)
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name