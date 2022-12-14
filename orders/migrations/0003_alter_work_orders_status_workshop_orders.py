# Generated by Django 4.1.1 on 2022-10-05 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_welli̇nformation_well_number'),
        ('orders', '0002_remove_assembly_orders_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_orders',
            name='status',
            field=models.CharField(choices=[('1', 'DEMONTAJ BEKLİYOR'), ('2', 'ATÖLYEDE'), ('3', 'TAMİR EDİLİYOR'), ('4', 'MONTAJ BEKLİYOR'), ('5', 'KAPANDI')], max_length=17, verbose_name='Durum'),
        ),
        migrations.CreateModel(
            name='Workshop_Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_orders_number', models.PositiveIntegerField(null=True, unique=True, verbose_name='Montaj numarası')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('invertory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.i̇nvertory', verbose_name='Envarter')),
                ('work_orders_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.work_orders', verbose_name='İş Emri')),
            ],
        ),
    ]
