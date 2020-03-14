from django.contrib import admin
from .models import Device, Client, Payment, Costs


class ShipmentAdmin(admin.ModelAdmin):

    search_fields = ['name']

class ClientAdmin(admin.ModelAdmin):

    autocomplete_fields = ['client']


class ShipmentAdmin2(admin.ModelAdmin):

    search_fields = ['name']


admin.site.register(Device,ShipmentAdmin2)
admin.site.register(Client,ShipmentAdmin)
admin.site.register(Payment,ClientAdmin)
admin.site.register(Costs)
