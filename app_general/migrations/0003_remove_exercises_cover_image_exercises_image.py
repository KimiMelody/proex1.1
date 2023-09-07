# Generated by Django 4.1.7 on 2023-04-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0002_exercises_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercises',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='exercises',
            name='image',
            field=models.ImageField(default='img.jpg', null='img.jpg', upload_to='cover_image/'),
            preserve_default='img.jpg',
        ),
    ]
