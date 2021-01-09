# Generated by Django 3.1.5 on 2021-01-09 06:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imageDescription', models.CharField(max_length=450)),
                ('image_url', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]