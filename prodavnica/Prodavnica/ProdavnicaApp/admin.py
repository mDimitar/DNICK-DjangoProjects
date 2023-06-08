from django.contrib import admin
from .models import Category,Product,Sale,SaleItem,Customer
# Register your models here.\

class ProductInlineCategory(admin.StackedInline):
    model = Product
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    inlines = [ProductInlineCategory,]
    list_display = ["name"]
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):

    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    def has_change_permission(self, request, obj=None):
        if obj:
            if obj.user == request.user:
                return True
            return False
    def has_add_permission(self, request):
        return True

admin.site.register(Product,ProductAdmin)

class SaleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
admin.site.register(Sale, SaleAdmin)

class SaleItemAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
admin.site.register(SaleItem,SaleItemAdmin)

class CustomerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    list_display = ["first_name","last_name"]
admin.site.register(Customer,CustomerAdmin)

