# Generated by Django 4.1.7 on 2023-03-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0001_initial'),
        ('app_exercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='m00a000',
            name='ref_id',
        ),
        migrations.AddField(
            model_name='m00a000',
            name='ref_id',
            field=models.ManyToManyField(to='app_general.exercises'),
        ),
    ]
