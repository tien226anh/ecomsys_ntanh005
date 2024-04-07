from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ClothCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to="images/cloth/")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ManyToManyField(ClothCategory)

    def __str__(self):
        return self.name
