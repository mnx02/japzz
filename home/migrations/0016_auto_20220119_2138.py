# Generated by Django 3.2.7 on 2022-01-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220119_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='female',
        ),
        migrations.RemoveField(
            model_name='register',
            name='male',
        ),
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('male', 'Man'), ('female', 'Woman')], default='male', max_length=100),
        ),
    ]
