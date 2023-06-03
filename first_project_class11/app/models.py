from django.db import models

# Create your models here.
class Banner(models.Model):
    title  = models.CharField(max_length = 150)
    url = models.URLField(max_length = 200)
    company_name  = models.CharField(max_length = 250, default='belal')
    image = models.ImageField(upload_to='BannerImage',default='no_image.jpg')
    
    

    def __str__(self):
        return self.title