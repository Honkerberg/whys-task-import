from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AttributeNameViewSet,
    AttributeValueViewSet,
    AttributeViewSet,
    CatalogViewSet,
    ImageViewSet,
    ImportViewSet,
    ProductAttributeViewSet,
    ProductImageViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router_import = DefaultRouter()

router_import.register("import", ImportViewSet, basename="import")
router.register("attributename", AttributeNameViewSet)
router.register("attribute", AttributeViewSet)
router.register("attributevalue", AttributeValueViewSet)
router.register("catalog", CatalogViewSet)
router.register("image", ImageViewSet)
router.register("product", ProductViewSet)
router.register("productattribute", ProductAttributeViewSet)
router.register("productimage", ProductImageViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(router_import.urls)),
]

urlpatterns = [
    path(r"detail/", include(router.urls)),
    path(r"", include(router_import.urls)),
]
