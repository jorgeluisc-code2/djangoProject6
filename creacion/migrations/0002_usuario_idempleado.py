# Generated by Django 3.1.3 on 2020-11-07 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='idempleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='creacion.empleado'),
        ),
    ]
