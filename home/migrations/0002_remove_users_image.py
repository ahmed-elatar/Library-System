# Generated by Django 3.2.7 on 2021-10-06 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
    ]