# Generated by Django 3.1.4 on 2020-12-16 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201216_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
