from django.contrib import admin

from .models import (
    Attribute,
    AttributeName,
    AttributeValue,
    Catalog,
    Image,
    Product,
    ProductAttributes,
    ProductImage,
)


@admin.register(AttributeName)
class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "kod", "zobrazit"]


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ["id", "hodnota"]


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev_atributu_id", "hodnota_atributu_id"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "cena", "mena", "published_on", "is_published"]


@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ["id", "attribute", "product"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "obrazek"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "product", "obrazek_id"]


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["id", "nazev", "obrazek_id"]
