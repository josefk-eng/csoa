# Generated by Django 4.1.7 on 2023-05-01 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csoa', '0004_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=500)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Introduction',
                'verbose_name_plural': 'Introduction',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('big_description', models.CharField(max_length=2000)),
                ('cordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csoa.member')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='CSOAImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='csoa/images')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csoa.project')),
            ],
            options={
                'verbose_name': 'CSOAImages',
                'verbose_name_plural': 'CSOAImages',
            },
        ),
        migrations.CreateModel(
            name='CSOACards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=2000)),
                ('footer', models.CharField(max_length=200)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csoa.project')),
            ],
            options={
                'verbose_name': 'CSOACards',
                'verbose_name_plural': 'CSOACards',
            },
        ),
    ]
