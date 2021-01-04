# Generated by Django 3.1.4 on 2020-12-13 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('overview', models.CharField(max_length=300)),
                ('content', tinymce.models.HTMLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('video_link', embed_video.fields.EmbedVideoField()),
                ('featured', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
            ],
        ),
    ]