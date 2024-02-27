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
    list_display = ["nazev", "kod", "zobrazit"]


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ["hodnota"]


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["nazev_atributu", "hodnota_atributu"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["nazev", "cena", "mena", "published_on", "is_published"]


@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ["attribute", "product"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["nazev", "obrazek"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["nazev", "product", "obrazek"]


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["nazev", "obrazek_id"]
