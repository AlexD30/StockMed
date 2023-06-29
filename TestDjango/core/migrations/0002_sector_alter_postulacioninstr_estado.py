# Generated by Django 4.0.4 on 2023-06-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('idSector', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de sector')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de sector')),
                ('descripcionSector', models.CharField(max_length=50, verbose_name='Descripcion de sector')),
                ('sucursal', models.CharField(max_length=50, verbose_name='Sucursal')),
            ],
        ),
        migrations.AlterField(
            model_name='postulacioninstr',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=50, verbose_name='estado de postulante'),
        ),
    ]