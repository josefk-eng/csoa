# Generated by Django 4.1.7 on 2023-05-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoweare', '0002_alter_history_image_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='group',
            field=models.CharField(default='', max_length=100),
        ),
    ]