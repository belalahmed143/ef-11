# Generated by Django 4.2.1 on 2023-06-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_service_options_service_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
