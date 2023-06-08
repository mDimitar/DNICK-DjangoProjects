from django.contrib import admin
from .models import Car,Manufacturer,Workshop,Repair,ManufacturerWorkshop

# Register your models here.

class ManufacturerWorkshopAdmin(admin.StackedInline):
    model = ManufacturerWorkshop
    extra = 0

class CarAdmin(admin.ModelAdmin):
    list_display = ["type","maxSpeed"]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Car,CarAdmin)

class WorkshopAdmin(admin.ModelAdmin):
    inlines = [ManufacturerWorkshopAdmin,]
    list_display = ["name","creationDate","fixesOldtimer"]

    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Workshop,WorkshopAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Manufacturer,ManufacturerAdmin)

class RepairAdmin(admin.ModelAdmin):
    list_display = ["code","date","description","workshop"]
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Repair,RepairAdmin)

