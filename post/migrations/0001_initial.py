# Generated by Django 3.2.5 on 2021-07-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('phone_number', models.DecimalField(decimal_places=15, max_digits=15)),
            ],
        ),
    ]
