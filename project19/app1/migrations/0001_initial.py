# Generated by Django 5.1.2 on 2024-11-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=12)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
