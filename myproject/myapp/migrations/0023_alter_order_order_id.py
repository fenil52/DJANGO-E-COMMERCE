# Generated by Django 5.0.1 on 2024-03-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_order_order_id_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
