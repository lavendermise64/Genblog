# Generated by Django 4.2.4 on 2023-08-18 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blogTittle',
            new_name='blogTitle',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 12, 19, 2, 81653, tzinfo=datetime.timezone.utc)),
        ),
    ]