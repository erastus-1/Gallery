from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    imageDescription = models.CharField(max_length=450)
    # image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    image_url = CloudinaryField('image', blank=True)   
    date_uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['date_uploaded']

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category