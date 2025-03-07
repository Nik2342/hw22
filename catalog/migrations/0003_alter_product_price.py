# Generated by Django 5.1.6 on 2025-03-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_created_at_alter_product_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="Введите цену за покупку",
                max_digits=10,
                null=True,
                verbose_name="Цена за покупку",
            ),
        ),
    ]
