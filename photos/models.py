from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField('Category')
    description = models.CharField(max_length=450)
    location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    image_url = CloudinaryField('image', blank=True)   
    date_uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['date_uploaded']

    def save_image(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location