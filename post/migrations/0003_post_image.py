# Generated by Django 3.2.5 on 2021-07-16 17:32

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=post.models.image_upload),
            preserve_default=False,
        ),
    ]
