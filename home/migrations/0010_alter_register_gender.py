# Generated by Django 3.2.7 on 2022-01-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220119_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.BooleanField(default=False, verbose_name='Other'),
        ),
    ]