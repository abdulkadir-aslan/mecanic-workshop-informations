# Generated by Django 4.1.1 on 2022-10-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_assembly_orders_status_disassembly_orders_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_orders',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Açıklama'),
        ),
    ]