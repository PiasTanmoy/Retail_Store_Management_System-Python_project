from django.contrib import admin
from .models import Payment, Order, Order_Detail

# Register your models here.
admin.site.register([Payment, Order, Order_Detail])