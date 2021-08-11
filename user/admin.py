from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","sta","prem","vip","expiredate","category","phone_number"]
    list_editable = ["category","sta","prem","vip"]

admin.site.register(Profile,ProfileAdmin)
admin.site.site_header = "EazyMax"
admin.site.site_title = "EazyMax"