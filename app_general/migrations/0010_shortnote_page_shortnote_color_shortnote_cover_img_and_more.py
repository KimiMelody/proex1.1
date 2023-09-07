# Generated by Django 4.1.7 on 2023-09-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0009_shortnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='shortnote_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortnote_id', models.IntegerField()),
                ('page', models.IntegerField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='media/images/shortnote/shortnote_page')),
            ],
        ),
        migrations.AddField(
            model_name='shortnote',
            name='color',
            field=models.CharField(max_length=7, null='#D9D9D9'),
            preserve_default='#D9D9D9',
        ),
        migrations.AddField(
            model_name='shortnote',
            name='cover_img',
            field=models.ImageField(blank=True, default=None, upload_to='media/images/shortnote/shortnote_cover'),
        ),
        migrations.AddField(
            model_name='shortnote',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]