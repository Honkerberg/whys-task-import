from django.db import models


class AttributeName(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True)
    kod = models.CharField(max_length=100, null=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}"


class AttributeValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    hodnota = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id}"


class Attribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=3, default='CZK')
    published_on = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}"


class ProductAttributes(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True)
    obrazek = models.URLField(null=True)

    def __str__(self) -> str:
        return f"{self.id}"


class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=100)


class Catalog(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100, blank=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    products_ids = models.ManyToManyField(Product, related_name='catalogs', blank=True)
    attributes_ids = models.ManyToManyField(Attribute, related_name='catalogs', blank=True)

    def __str__(self) -> str:
        return self.nazev
