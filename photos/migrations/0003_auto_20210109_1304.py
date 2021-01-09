# Generated by Django 3.1.5 on 2021-01-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210109_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='photos.Category'),
        ),
    ]