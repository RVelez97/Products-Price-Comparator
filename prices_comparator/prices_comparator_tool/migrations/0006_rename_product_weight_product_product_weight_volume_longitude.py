# Generated by Django 5.0.7 on 2024-07-16 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices_comparator_tool', '0005_productcategory_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_weight',
            new_name='product_weight_volume_longitude',
        ),
    ]
