# Generated by Django 4.1.4 on 2022-12-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes_app', '0002_alter_routesmodel_bus_id_alter_routesmodel_driver_id'),
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='route_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_route', to='routes_app.routesmodel'),
        ),
    ]
