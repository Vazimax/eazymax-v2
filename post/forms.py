from django.utils.translation import ugettext_lazy 
from django import forms
from .models import Post 
from user.models import Profile

import datetime , timedelta , timezones

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length="100",label= ugettext_lazy('post title'))
    description = forms.CharField(max_length="1000",label= ugettext_lazy('description'))
    phone_number = forms.CharField(required=True,label= ugettext_lazy('phone number'))

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['poster','date_posted','hot']
        # def has_posted_today(self):
        #   yesterday = timezones.now() - timezones.timedelta(hours=24)
        #   poster = self.cleaned_data.get('poster')
        #   if Post.objects.filter(poster=poster, post_date__gt=yesterday).exists():
        #       raise forms.ValidationError("You have already posted today, Come back tomorrow!")

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.title = self.cleaned_data["title"]
        post.description = self.cleaned_data["description"]
        post.phone_number = self.cleaned_data["phone_number"]
        if commit:
            post.save()
        return post

