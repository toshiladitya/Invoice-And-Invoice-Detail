from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    
    