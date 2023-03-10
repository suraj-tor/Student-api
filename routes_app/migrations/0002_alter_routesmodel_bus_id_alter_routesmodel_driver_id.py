# Generated by Django 4.1.4 on 2022-12-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0001_initial'),
        ('driver_app', '0001_initial'),
        ('routes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routesmodel',
            name='bus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_bus', to='vehicle_app.bus'),
        ),
        migrations.AlterField(
            model_name='routesmodel',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_driver', to='driver_app.driver'),
        ),
    ]
