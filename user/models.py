from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from post.models import Category
import datetime

class sta(models.Model):
    sub = models.BooleanField(default=False)
    
   
class prem(models.Model):
    sub = models.BooleanField(default=False)

    
class vip(models.Model):
    sub = models.BooleanField(default=False)

   
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,help_text=_('user'))
    sta=models.BooleanField(sta,default=False)
    prem=models.BooleanField(prem,default=False)
    vip=models.BooleanField(vip,default=False)
    expiredate= models.DateField(null=True,blank=True)
    maxd=models.BooleanField(default=False)


    phone_number = models.CharField(max_length=20,help_text=_('phone_number'),null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoryx',default=1,help_text=_('category'))
    image = models.ImageField(upload_to="profile/",default="profile/default.jpg",help_text=_('image'))
    

    def __str__(self):
        return str(self.user)
        

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


