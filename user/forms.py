from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy 
from .models import Profile 



class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length="100",label= ugettext_lazy('firstname'))
    lastname = forms.CharField(max_length="100",label= ugettext_lazy('lastname'))
    email = forms.EmailField(required=False,label= ugettext_lazy('email'))
    

    class Meta:
        model = User
        fields = ['firstname','lastname','username','email','password1','password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length="100",label= ugettext_lazy('phone number'))

    class Meta:
        model = Profile
        fields = ['phone_number','category','image']

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        profile.phone_number = self.cleaned_data["phone_number"]
        if commit:
            profile.save()
        return profile