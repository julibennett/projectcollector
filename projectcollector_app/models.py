from django.db import models
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    technologies = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    live = models.CharField(max_length=150)
    created = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
