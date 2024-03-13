# Generated by Django 5.0.1 on 2024-03-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='bestseller_img')),
                ('product_name', models.CharField(max_length=800)),
                ('product_price', models.PositiveIntegerField()),
                ('prodcut_details', models.TextField()),
                ('extra_img1', models.ImageField(blank=True, null=True, upload_to='product_view_slider_img/')),
                ('extra_img2', models.ImageField(blank=True, null=True, upload_to='product_view_slider_img/')),
                ('extra_img3', models.ImageField(blank=True, null=True, upload_to='product_view_slider_img/')),
                ('extra_img4', models.ImageField(blank=True, null=True, upload_to='product_view_slider_img/')),
                ('extra_img5', models.ImageField(blank=True, null=True, upload_to='product_view_slider_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Mainslider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='main_slider_img/')),
                ('img2', models.ImageField(upload_to='main_slider_img/')),
                ('img3', models.ImageField(upload_to='main_slider_img/')),
            ],
        ),
    ]