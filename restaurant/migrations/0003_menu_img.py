# Generated by Django 5.0.7 on 2024-08-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(default=1, upload_to='static/img/ipload_images'),
            preserve_default=False,
        ),
    ]
