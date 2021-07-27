from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from PIL import Image


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

def image_upload(instance , filename):
    imagename , extension = filename.split('.')

    return f"jobs/{instance.id}.{extension}"

class Post(models.Model):
    title = models.CharField(max_length=100,)
    poster = models.ForeignKey(User,related_name='job_poster',on_delete=models.CASCADE,)
    description = models.TextField(max_length=10000,null=True,blank=True,)
    phone_number = models.IntegerField(null=True,blank=True)
    category = models.ForeignKey(Category,related_name='categories',on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=image_upload,default="jobs/default.jpg",null=True,blank=True,)
    date_posted = models.DateTimeField(auto_now=True)
    hot=models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})