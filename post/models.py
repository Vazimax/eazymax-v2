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
    phone_number = models.CharField(null=True,blank=True,max_length=15)
    category = models.ForeignKey(Category,related_name='categories',on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=image_upload,default="jobs/default.jpg",null=True,blank=True,)
    date_posted = models.DateTimeField(auto_now=True)
    hot=models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

RATE_CHOICES = [
    (1,'1 - Terrible/فظيع'),
    (2,'2 - Mauvais(e)/سيء'),
    (3,'3 - Pas mal/ليس سيئا'),
    (4,'4 - bon(ne)/جيد'),
    (5,'5 - génial(e)/ممتاز'),
]

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000,blank=True,null=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES,blank=True)

    def __str__(self):
        return self.user.username