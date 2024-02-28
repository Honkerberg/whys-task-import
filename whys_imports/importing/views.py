from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

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
from .serializers import (
    AttributeNameSerializer,
    AttributeSerializer,
    AttributeValueSerializer,
    CatalogSerializer,
    ImageSerializer,
    ProductAttributesSerializer,
    ProductImageSerializer,
    ProductSerializer,
)


class ImportList(CreateAPIView):
    """
    Import all data and parse through serializers.
    """


class AttributeNameViewSet(ModelViewSet):
    queryset = AttributeName.objects.all()
    serializer_class = AttributeNameSerializer


class AttributeViewSet(ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeValueViewSet(ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class CatalogViewSet(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAttributeViewSet(ModelViewSet):
    queryset = ProductAttributes.objects.all()
    serializer_class = ProductAttributesSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
