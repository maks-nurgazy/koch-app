# Generated by Django 3.1.3 on 2021-06-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0007_cargo_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='volume',
            field=models.FloatField(),
        ),
    ]
