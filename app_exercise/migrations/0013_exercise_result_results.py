# Generated by Django 4.1.7 on 2023-06-11 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_exercise', '0012_remove_exercise_result_user_remove_result_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_result',
            name='results',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='app_exercise.result'),
        ),
    ]
