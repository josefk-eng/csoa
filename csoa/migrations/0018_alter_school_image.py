# Generated by Django 4.1.7 on 2023-05-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csoa', '0017_school_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='image',
            field=models.ImageField(default='img/placeholder.jpeg', upload_to='img/schools'),
        ),
    ]
