from django.db import models

# Projects Model to store project name, description and image


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/project_images/', null=True, max_length=255)
    project_url = models.URLField(max_length=200, default='http://www.google.com')
