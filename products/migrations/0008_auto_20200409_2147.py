# Generated by Django 3.0.5 on 2020-04-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200409_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
