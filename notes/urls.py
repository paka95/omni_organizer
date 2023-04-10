from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='notes'),
    path('', views.Index.as_view(), name="notes"),
    path('get-notes/', views.GetNotes.as_view(), name="get-notes")
]