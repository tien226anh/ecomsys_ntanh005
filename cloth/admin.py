from django.contrib import admin

from cloth.models import Cloth, ClothCategory, Manufacturer

# Register your models here.
admin.site.register(Cloth)
admin.site.register(ClothCategory)
admin.site.register(Manufacturer)
