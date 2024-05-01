from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    technologies = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    live = models.CharField(max_length=150)
    created = models.CharField(max_length=100)

    def __str__(self):
        return self.name
