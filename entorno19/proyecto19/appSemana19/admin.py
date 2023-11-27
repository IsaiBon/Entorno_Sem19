from django.contrib import admin

# Register your models here.
from .models import Proveedores
from .models import Productos

admin.site.register(Proveedores)
admin.site.register(Productos)