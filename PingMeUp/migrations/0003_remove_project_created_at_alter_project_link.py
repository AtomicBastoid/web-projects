# Generated by Django 5.2 on 2025-04-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PingMeUp', '0002_alter_project_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
