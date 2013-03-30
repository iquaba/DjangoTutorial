from django.contrib import admin
from certs.models import Cert, Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'website',)
    search_fields = ('name',)

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Cert)
