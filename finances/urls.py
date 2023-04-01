from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='finances'),
    path('get-expenses/', views.GetExpenses.as_view(), name='get-expenses'),
    path('submit/', views.SubmitExpense.as_view(), name='submit-expense'),
    path('delete/<int:pk>/', views.DeleteExpense.as_view(), name='delete-expense'),
    path('update/<int:pk>/', views.UpdateExpense.as_view(), name='update-expense'),
]