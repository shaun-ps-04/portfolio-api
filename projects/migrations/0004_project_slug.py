# Generated by Django 4.1.1 on 2022-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_description_alter_project_imageuri'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True, unique=True),
        ),
    ]
