from django.db import models

# Create your models here.
class Banner(models.Model):
    title  = models.CharField(max_length = 150)
    url = models.URLField(max_length = 200)
    company_name  = models.CharField(max_length = 250, default='belal')
    image = models.ImageField(upload_to='BannerImage',default='no_image.jpg')
    
    def __str__(self):
        return self.title

class ServiceCategory(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title  = models.CharField(max_length = 150)
    image  = models.ImageField(upload_to='ServiceImage')
    category  = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price  = models.IntegerField(default=444)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class ContactUs(models.Model):
    name  = models.CharField(max_length = 150)
    email  = models.CharField(max_length = 150)
    message = models.TextField()
    
    
    
    
    
    