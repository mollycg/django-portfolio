from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)
    repo = models.URLField(blank=True)

    def __str__(self):
        return self.name