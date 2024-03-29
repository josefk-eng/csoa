# Generated by Django 4.1.7 on 2023-05-01 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('csoa', '0006_partners_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('impacted', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscriber',
            },
        ),
        migrations.CreateModel(
            name='LatestEngagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'LatestEngagement',
                'verbose_name_plural': 'LatestEngagement',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('secondName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=1000)),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscriber',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('engagement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csoa.latestengagement')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.AddField(
            model_name='csoaimages',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csoa.csoacards'),
        ),
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(default='img/placeholder1.png', upload_to='img/schools'),
        ),
        migrations.AlterField(
            model_name='csoacards',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='csoaimages',
            name='image',
            field=models.ImageField(default='img/placeholder1.png', upload_to='img/images'),
        ),
        migrations.AlterField(
            model_name='csoaimages',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(upload_to='img/partners'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='impact',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csoa.csoacards'),
        ),
        migrations.AddField(
            model_name='csoaimages',
            name='engagement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='csoa.latestengagement'),
        ),
    ]
