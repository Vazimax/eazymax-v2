# Generated by Django 3.2.5 on 2021-08-13 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0019_alter_post_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('rate', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 - Terrible/فظيع'), (2, '2 - Mauvais(e)/سيء'), (3, '3 - Pas mal/ليس سيئا'), (4, '4 - bon(ne)/جيد'), (5, '5 - génial(e)/ممتاز')])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]