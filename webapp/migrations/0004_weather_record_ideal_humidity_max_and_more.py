# Generated by Django 5.0.6 on 2024-06-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_record_price_alter_record_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_humidity_max',
            field=models.FloatField(default=70),
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_humidity_min',
            field=models.FloatField(default=35),
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_rainfall_max',
            field=models.FloatField(default=800),
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_rainfall_min',
            field=models.FloatField(default=300),
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_temperature_max',
            field=models.FloatField(default=35),
        ),
        migrations.AddField(
            model_name='record',
            name='ideal_temperature_min',
            field=models.FloatField(default=20),
        ),
    ]