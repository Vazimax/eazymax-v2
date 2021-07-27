# Generated by Django 3.2.5 on 2021-07-26 03:07

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210722_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='prem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='vip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='featured',
        ),
        migrations.AddField(
            model_name='profile',
            name='dated',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='expiredate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='max',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='prem',
            field=models.BooleanField(default=False, verbose_name=user.models.prem),
        ),
        migrations.AddField(
            model_name='profile',
            name='sta',
            field=models.BooleanField(default=False, verbose_name=user.models.sta),
        ),
        migrations.AddField(
            model_name='profile',
            name='vip',
            field=models.BooleanField(default=False, verbose_name=user.models.vip),
        ),
    ]