# Generated by Django 3.1.3 on 2021-06-18 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210619_0524'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='PrivacyText',
        ),
    ]