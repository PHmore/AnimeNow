# Generated by Django 5.0.3 on 2024-06-11 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
