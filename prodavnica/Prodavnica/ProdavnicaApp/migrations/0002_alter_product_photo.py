# Generated by Django 4.2.1 on 2023-06-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProdavnicaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.URLField(),
        ),
    ]
