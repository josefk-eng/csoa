# Generated by Django 4.1.7 on 2023-05-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='img/placeholder.jpeg', upload_to='img/news'),
        ),
    ]
