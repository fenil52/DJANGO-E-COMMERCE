# Generated by Django 5.0.1 on 2024-03-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
