from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    #phone = models.CharField(max_length=20, blank=False, null=False)
    #email = models.EmailField(max_length=255, blank=False, null=False)
    #address = models.CharField(max_length=255, blank=False, null=False)
    logo = models.ImageField(upload_to='customers/logos', default="no_picture.png", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
