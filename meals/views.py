from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from .apps import MealsConfig
from django.views import View
import datetime
from .models import Product
from .serializers import ProductSerializer
from itertools import zip_longest


app_name = MealsConfig.name

class Index(View):
    template_name = 'meals/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class AddProduct(CreateAPIView):
    serializer_class = ProductSerializer