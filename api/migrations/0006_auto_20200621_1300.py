# Generated by Django 3.0.7 on 2020-06-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_project_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='project_url',
        ),
    ]
