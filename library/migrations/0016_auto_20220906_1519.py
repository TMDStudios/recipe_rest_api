# Generated by Django 3.2.7 on 2022-09-06 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20220906_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='about',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='api_key',
            field=models.CharField(blank=True, default='ca7a4fbc4584f0cfc5fb7d43459e198d0ac3f09c65789d2c7b0de1d1ce533e21', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='image',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='settings',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='website',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
