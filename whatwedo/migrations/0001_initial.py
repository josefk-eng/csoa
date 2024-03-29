# Generated by Django 4.1.7 on 2023-05-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/news')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
