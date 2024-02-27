from django.db import models


class AttributeName(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100)
    kod = models.CharField(max_length=100, null=True)
    zobrazit = models.BooleanField(default=False)


class AttributeValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    hodnota = models.CharField(max_length=100)


class Attribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev_atributu = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100)
    description = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=3)
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
    nazev = models.CharField(max_length=100, null=True)
    obrazek = models.URLField()


class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=100)


class Catalog(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazev = models.CharField(max_length=100)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    products_ids = models.ManyToManyField('Product', related_name='catalogs')
    attributes_ids = models.ManyToManyField('Attribute', related_name='catalogs')
