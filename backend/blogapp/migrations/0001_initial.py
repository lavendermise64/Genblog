# Generated by Django 4.2.4 on 2023-08-18 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTittle', models.CharField(max_length=150)),
                ('blogPost', models.TextField()),
                ('blogDate', models.DateTimeField(default=datetime.datetime(2023, 8, 18, 9, 49, 8, 548893, tzinfo=datetime.timezone.utc))),
                ('blogAuthor', models.CharField(max_length=50)),
            ],
        ),
    ]