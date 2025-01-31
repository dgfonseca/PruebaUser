# Generated by Django 3.0.4 on 2020-05-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camionero',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.FloatField(blank=True, default=None, primary_key=True, serialize=False)),
                ('telefono', models.FloatField(blank=True, default=None, null=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('numeroRunt', models.FloatField(blank=True, default=None, editable=False, null=True, unique=True)),
                ('sueldo', models.FloatField(blank=True, default=1500000)),
            ],
        ),
    ]
