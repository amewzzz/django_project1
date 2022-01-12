from django.db import models

# Create your models here
class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    
    
    def __str__(self):
        return self.title
