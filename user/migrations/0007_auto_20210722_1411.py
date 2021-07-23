# Generated by Django 3.2.5 on 2021-07-22 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0012_auto_20210721_1702'),
        ('user', '0006_alter_profile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.ForeignKey(default=1, help_text='category', on_delete=django.db.models.deletion.CASCADE, related_name='categoryx', to='post.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='featured',
            field=models.BooleanField(default=False, help_text='featured'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.jpg', help_text='image', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(help_text='phone_number', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(help_text='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
