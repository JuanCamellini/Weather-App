# Generated by Django 4.1 on 2022-12-06 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]