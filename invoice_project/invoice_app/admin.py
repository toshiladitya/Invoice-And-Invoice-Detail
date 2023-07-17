from django.contrib import admin
from .models import InvoiceDetail,Invoice
# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)