# Generated by Django 4.1.4 on 2022-12-31 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle_app', '0001_initial'),
        ('driver_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutesModel',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('from_place', models.CharField(max_length=100)),
                ('to_place', models.CharField(max_length=100)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_app.bus')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_app.driver')),
            ],
        ),
    ]