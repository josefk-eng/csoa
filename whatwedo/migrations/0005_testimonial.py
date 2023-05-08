# Generated by Django 4.1.7 on 2023-05-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatwedo', '0004_remove_prayer_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='img/placeholder.png', upload_to='img/tests')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('testimony', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]