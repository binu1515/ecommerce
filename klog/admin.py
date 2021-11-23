from django.contrib import admin
from .models import Categrory, customer, product, user

# Register your models here.
admin.site.register(user)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(Categrory)