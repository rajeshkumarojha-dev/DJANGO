# Generated by Django 5.1.2 on 2024-11-27 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='empNo',
        ),
    ]
