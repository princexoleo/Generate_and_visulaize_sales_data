from django.db import models
from django.shortcuts import reverse
from profiles.models import Profile

# Create your models here.
# A Report class model
class Report(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reports/', blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("reports:report_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['-created_at']
    
    
