# Generated by Django 4.0.3 on 2023-06-06 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0005_remove_automobilevo_manufacturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobilevo',
            name='color',
        ),
        migrations.RemoveField(
            model_name='automobilevo',
            name='model',
        ),
        migrations.RemoveField(
            model_name='automobilevo',
            name='year',
        ),
    ]
