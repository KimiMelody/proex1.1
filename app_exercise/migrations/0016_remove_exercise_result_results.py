# Generated by Django 4.1.7 on 2023-06-11 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_exercise', '0015_alter_exercise_result_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_result',
            name='results',
        ),
    ]
