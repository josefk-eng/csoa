# Generated by Django 4.1.7 on 2023-05-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_projectoverview'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectoverview',
            name='image',
            field=models.ImageField(default='img/placeholder.jpeg', upload_to='img/overview'),
        ),
    ]
