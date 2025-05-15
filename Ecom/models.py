from django.db import models

# Create your models here.

class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    vission = models.TextField(blank=True, null=True)
    banner_image = models.ImageField(upload_to='about/', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.description}'
    
    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'