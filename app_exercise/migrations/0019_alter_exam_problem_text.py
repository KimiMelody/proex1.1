# Generated by Django 4.1.7 on 2023-06-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_exercise', '0018_alter_exercise_result_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='problem_text',
            field=models.CharField(max_length=150),
        ),
    ]
