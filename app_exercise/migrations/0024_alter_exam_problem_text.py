# Generated by Django 4.1.7 on 2023-06-20 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_exercise', '0023_remove_exercise_result_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='problem_text',
            field=models.CharField(max_length=200),
        ),
    ]
