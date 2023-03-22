from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='finances'),
    path('', views.Index.as_view(), name='finances'),
]