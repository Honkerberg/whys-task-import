# Generated by Django 5.0.2 on 2024-02-28 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("importing", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="attribute",
            old_name="hodnota_atributu",
            new_name="hodnota_atributu_id",
        ),
        migrations.RenameField(
            model_name="attribute",
            old_name="nazev_atributu",
            new_name="nazev_atributu_id",
        ),
        migrations.RenameField(
            model_name="productimage",
            old_name="obrazek",
            new_name="obrazek_id",
        ),
        migrations.AlterField(
            model_name="attributename",
            name="nazev",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="attributes_ids",
            field=models.ManyToManyField(
                blank=True, related_name="catalogs", to="importing.attribute"
            ),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="nazev",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="obrazek_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="importing.image",
            ),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="products_ids",
            field=models.ManyToManyField(
                blank=True, related_name="catalogs", to="importing.product"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="nazev",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="image",
            name="obrazek",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="mena",
            field=models.CharField(default="CZK", max_length=3),
        ),
        migrations.AlterField(
            model_name="product",
            name="nazev",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
