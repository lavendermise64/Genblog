# Generated by Django 4.2.4 on 2023-08-21 12:50

import blogapp.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_blog_blogdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogImage',
            field=models.ImageField(default='blogs/default.png', upload_to=blogapp.models.upload_to, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 12, 50, 14, 105051, tzinfo=datetime.timezone.utc)),
        ),
    ]
