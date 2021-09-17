# Generated by Django 3.2.7 on 2021-09-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=1000)),
                ('instructions', models.CharField(max_length=1000)),
            ],
        ),
    ]
