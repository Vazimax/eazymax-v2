# Generated by Django 3.2.5 on 2021-07-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20210726_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]