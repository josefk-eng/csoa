# Generated by Django 4.1.7 on 2023-05-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csoa', '0016_latestengagement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='description',
            field=models.TextField(default=''),
        ),
    ]