from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name


class MobileCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to="images/mobile/", null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ManyToManyField(MobileCategory)

    def __str__(self):
        return self.name
