from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='projects/images/')  
    date_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.title
