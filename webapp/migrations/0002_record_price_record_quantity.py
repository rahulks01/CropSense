# Generated by Django 5.0.6 on 2024-06-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='price',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='record',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]