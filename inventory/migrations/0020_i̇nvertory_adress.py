# Generated by Django 4.1.1 on 2022-10-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_alter_i̇nvertory_well_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='i̇nvertory',
            name='adress',
            field=models.CharField(blank=True, max_length=50, verbose_name='Adres'),
        ),
    ]
