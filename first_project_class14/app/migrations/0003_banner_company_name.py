# Generated by Django 4.2.1 on 2023-05-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner_taka'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='company_name',
            field=models.CharField(default='belal', max_length=250),
        ),
    ]