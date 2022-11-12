# Generated by Django 4.1.1 on 2022-09-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engine',
            name='number',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='pump',
            name='number',
        ),
        migrations.RemoveField(
            model_name='pump',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='i̇nvertory',
            name='engine_serial_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Motor Seri Numarası'),
        ),
        migrations.AddField(
            model_name='i̇nvertory',
            name='pump_serial_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Pompa SeriNumarası'),
        ),
        migrations.AlterField(
            model_name='engine',
            name='engine_type',
            field=models.CharField(choices=[('1', '3"'), ('2', '4"'), ('3', '5"'), ('4', '6"'), ('5', '7"'), ('6', '8"'), ('7', '9"'), ('5', '10"'), ('6', '11"')], max_length=4, verbose_name='MotorTipi'),
        ),
        migrations.AlterField(
            model_name='i̇nvertory',
            name='tank_info',
            field=models.CharField(choices=[('1', 'TANK'), ('2', 'ŞEBEKE'), ('3', 'HAVUZ'), ('4', 'DEPO'), ('5', 'BOŞTA'), ('6', 'AYAKLI DEPO')], max_length=11, verbose_name='DepoBilgisi'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='pump_breed',
            field=models.CharField(choices=[('1', 'KROM'), ('2', 'NORİL'), ('3', 'DÖKÜM')], max_length=5, verbose_name='Cinsi'),
        ),
    ]
