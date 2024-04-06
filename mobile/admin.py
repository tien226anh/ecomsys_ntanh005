from django.contrib import admin

from mobile.models import Manufacturer, Mobile, MobileCategory

# Register your models here.
admin.site.register(Mobile)
admin.site.register(Manufacturer)
admin.site.register(MobileCategory)