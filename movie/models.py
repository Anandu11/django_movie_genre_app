from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.IntegerField()  
    summary = models.TextField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
