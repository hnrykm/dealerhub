# Generated by Django 4.0.3 on 2023-06-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0003_alter_automobilevo_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilevo',
            name='import_href',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='automobilevo',
            name='model',
            field=models.CharField(default='', max_length=300),
        ),
    ]
