# Generated by Django 4.2.5 on 2023-10-21 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(upload_to='Banner/'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='photo',
            field=models.ImageField(upload_to='Banner/'),
        ),
    ]
