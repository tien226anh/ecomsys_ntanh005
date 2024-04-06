# Generated by Django 4.1.13 on 2024-04-05 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='MobileCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images/mobile/')),
                ('category', models.ManyToManyField(to='mobile.mobilecategory')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.manufacturer')),
            ],
        ),
    ]
