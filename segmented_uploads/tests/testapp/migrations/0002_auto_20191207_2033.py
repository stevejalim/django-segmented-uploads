# Generated by Django 3.0 on 2019-12-08 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
