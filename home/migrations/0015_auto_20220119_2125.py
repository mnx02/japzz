# Generated by Django 3.2.7 on 2022-01-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220119_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='female',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='male',
            field=models.BooleanField(default=False),
        ),
    ]