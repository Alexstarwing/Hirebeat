# Generated by Django 3.2.8 on 2023-08-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Management', '0002_auto_20230802_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]