# Generated by Django 4.1.7 on 2023-05-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoweare', '0003_portfolio_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
