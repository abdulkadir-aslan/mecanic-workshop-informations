# Generated by Django 4.0.4 on 2022-10-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_work_orders_job_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_orders',
            name='job_done',
            field=models.CharField(max_length=300, verbose_name='iş akışı'),
        ),
    ]
