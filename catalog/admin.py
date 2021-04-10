from django.contrib import admin

# Register your models here.
from django.contrib import admin
from catalog.models import Customer
from catalog.models import Supplier
#from catalog.models import Cart

admin.site.register(Customer)
admin.site.register(Supplier)
#admin.site.register(Cart)