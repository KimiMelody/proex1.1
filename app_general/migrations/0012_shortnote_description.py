# Generated by Django 4.1.7 on 2023-09-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0011_rename_cover_img_shortnote_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortnote',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
