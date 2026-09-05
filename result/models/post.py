from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Phones(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    tags = TaggableManager()
    image = models.ImageField(upload_to='result/',default='result/default.jpg')
    context = models.TextField(max_length=225)
    status = models.BooleanField(default=True)  
    price = models.PositiveIntegerField()
    memory = models.PositiveIntegerField()
    network = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.name