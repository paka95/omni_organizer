from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="notes"),
    path('get-notes/', views.GetNotes.as_view(), name="get-notes"),
    path('submit/', views.SubmitNote.as_view(), name='submit-note'),
    path('delete/<int:pk>/', views.DeleteNote.as_view(), name='delete-note'),
]