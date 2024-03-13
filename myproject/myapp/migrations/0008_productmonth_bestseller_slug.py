# Generated by Django 5.0.1 on 2024-03-06 13:47

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_img', models.ImageField(upload_to='product_of_month/')),
                ('month_name', models.CharField(max_length=480)),
                ('month_description', models.TextField(blank=True, null=True)),
                ('month_prcie', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bestseller',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True),
        ),
    ]
