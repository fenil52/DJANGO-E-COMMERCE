# Generated by Django 5.0.1 on 2024-03-07 03:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_insta_post_insta_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmonth',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='month_name', unique=True),
        ),
    ]
