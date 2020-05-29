# Generated by Django 3.0.6 on 2020-05-29 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Camion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSolicitud', models.CharField(default=None, max_length=6)),
                ('fechaEntrega', models.CharField(default=None, max_length=6)),
                ('tienda', models.IntegerField(default=None)),
                ('camion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Camion.Camion')),
            ],
        ),
    ]
