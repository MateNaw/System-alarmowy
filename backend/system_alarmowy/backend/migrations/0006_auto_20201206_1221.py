# Generated by Django 3.1.3 on 2020-12-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20201206_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='gas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
