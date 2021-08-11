from django.contrib import admin
from .models import Post , Category


class PostAdmin(admin.ModelAdmin):
    list_display = ["title","poster","phone_number","category","hot","date_posted"]
    list_editable = ["category","hot"]

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
