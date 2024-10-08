# Generated by Django 5.0.7 on 2024-07-15 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices_comparator_tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='produc_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_unis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='prices_comparator_tool.productcategory'),
            preserve_default=False,
        ),
    ]
