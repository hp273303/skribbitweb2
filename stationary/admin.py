from django.contrib import admin
from stationary.models import Product
# Register your models here.
class ProductAdmin (admin.ModelAdmin):
    list_display=('name','image_url','price','description','category')
    
admin.site.register(Product,ProductAdmin)

