# Generated by Django 4.1.4 on 2022-12-31 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_rename_studentmodel_student'),
        ('driver_app', '0001_initial'),
        ('vehicle_app', '0001_initial'),
        ('routes_app', '0002_alter_routesmodel_bus_id_alter_routesmodel_driver_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoutesModel',
            new_name='Route',
        ),
    ]
