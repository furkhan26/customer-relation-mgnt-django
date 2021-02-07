from django.contrib import admin

# Register your models here.
from .models import Tag,Customer,Product,Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)