# Generated by Django 5.0.6 on 2024-09-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tasks_delete_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
