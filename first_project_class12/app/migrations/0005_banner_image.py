# Generated by Django 4.2.1 on 2023-05-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_banner_taka'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='no_image.jpg', upload_to='BannerImage'),
        ),
    ]
