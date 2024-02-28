from rest_framework import serializers

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


class AttributeNameSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField(required=False)

    class Meta:
        model = AttributeName
        fields = ["nazev", "kod", "zobrazit"]


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["nazev_atributu_id", "hodnota_atributu_id"]

    def to_representation(self, instance):
        self.fields["nazev_atributu_id"] = AttributeNameSerializer(read_only=True)
        self.fields["hodnota_atributu_id"] = AttributeValueSerializer(read_only=True)
        return super(AttributeSerializer, self).to_representation(instance)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["attribute"] = AttributeSerializer(read_only=True)
        return super(ProductAttributesSerializer, self).to_representation(instance)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["product"] = ProductSerializer(read_only=True)
        self.fields["obrazek_id"] = ImageSerializer(read_only=True)
        return super(ProductImageSerializer, self).to_representation(instance)


class CatalogSerializer(serializers.ModelSerializer):
    products_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, required=False
    )
    attributes_ids = serializers.PrimaryKeyRelatedField(
        queryset=Attribute.objects.all(), many=True, required=False
    )

    class Meta:
        model = Catalog
        fields = ["nazev", "obrazek_id", "products_ids", "attributes_ids"]

    def create(self, validated_data):
        products_data = validated_data.pop("products_ids", [])
        attributes_data = validated_data.pop("attributes_ids", [])

        catalog = Catalog.objects.create(**validated_data)

        catalog.products_ids.set(products_data)
        catalog.attributes_ids.set(attributes_data)

        return catalog

    def to_representation(self, instance):
        self.fields["obrazek_id"] = ImageSerializer(read_only=True)
        return super().to_representation(instance)
