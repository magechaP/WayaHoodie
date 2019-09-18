# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-18 04:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=64, unique=True)),
                ('business_email', models.EmailField(max_length=64, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('descriptive_image', models.ImageField(default='photos/default_biz.jpg', upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50, null=True)),
                ('members_count', models.IntegerField(default=0, null=True)),
                ('police_dept', models.CharField(max_length=50)),
                ('police_dept_address', models.CharField(max_length=50)),
                ('health_dept', models.CharField(max_length=50)),
                ('health_dept_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=500)),
                ('descriptive_picture', models.ImageField(default='photos/default_post.jpg', upload_to='photos/')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_hood', to='hood.Neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(default='photos/default.jpg', upload_to='photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('contact', models.CharField(max_length=12)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people_count', to='hood.Neighbourhood')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Profile'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='headman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='biz_hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='biz_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]