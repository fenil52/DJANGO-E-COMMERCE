# Generated by Django 5.0.1 on 2024-03-06 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestseller',
            old_name='prodcut_details',
            new_name='product_details',
        ),
    ]
