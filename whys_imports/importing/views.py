from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import status

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


class ImportViewSet(ViewSet):
    """
    Import all data and parse through serializers.
    """    
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            for item in data:
                if 'AttributeName' in item:
                    serializer = AttributeNameSerializer(data=item['AttributeName'])
                elif 'AttributeValue' in item:
                    serializer = AttributeValueSerializer(data=item['AttributeValue'])
                if 'Attribute' in item:
                    serializer = AttributeSerializer(data=item['Attribute'])
                elif 'Product' in item:
                    serializer = ProductSerializer(data=item['Product'])
                elif 'ProductAttributes' in item:
                    serializer = ProductAttributesSerializer(data=item['ProductAttributes'])
                elif 'Catalog' in item:
                    serializer = CatalogSerializer(data=item['Catalog'])
                elif 'Image' in item:
                    serializer = ImageSerializer(data=item['Image'])
                elif 'ProductImage' in item:
                    serializer = ProductImageSerializer(data=item['ProductImage'])
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({"message": f"Error importing data {serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Data imported successfully"})
        except KeyError as e:
            return Response({"message": f"Error importing data {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        


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
