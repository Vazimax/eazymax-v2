from django.utils.translation import ugettext_lazy
from django import forms
from .models import Post
import django_filters

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',label= ugettext_lazy('what are you looking for ..?'),widget=forms.TextInput(attrs={'placeholder':'Que cherche-tu ? / عما تبحث ؟'}))
    class Meta:
        model = Post
        fields = ['title','category']

class JobFilter2(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',label= ugettext_lazy('what are you looking for ..?'),widget=forms.TextInput(attrs={}))
    class Meta:
        model = Post
        fields = ['title']
