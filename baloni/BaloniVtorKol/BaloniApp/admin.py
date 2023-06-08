from django.contrib import admin
from .models import Pilot,AeroCompany,Ballon,Fligth,PilotsInAeroCompany

# Register your models here.

class PilotsInAeroCompanyAdmin(admin.StackedInline):
    model = PilotsInAeroCompany
    extra = 0

class PilotAdmin(admin.ModelAdmin):
    list_display = ["name","surname"]

admin.site.register(Pilot,PilotAdmin)

class AeroCompanyAdmin(admin.ModelAdmin):
    inlines = [PilotsInAeroCompanyAdmin]
    list_display = ["name"]

admin.site.register(AeroCompany,AeroCompanyAdmin)

class BallonAdmin(admin.ModelAdmin):
    list_display = ["type","manufacturerName"]

admin.site.register(Ballon,BallonAdmin)

class FlightAdmin(admin.ModelAdmin):
    list_display = ["code","balloon","pilot","aeroCompany"]

    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Fligth,FlightAdmin)