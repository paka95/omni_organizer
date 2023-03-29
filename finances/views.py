from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.db.models import Sum
from .apps import FinancesConfig
from django.http import JsonResponse
from django.views import View
import json, datetime
from .models import Expense
from .serializers import ExpenseSerializer


app_name = FinancesConfig.name

class Index(View):
    template_name = 'finances/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class GetExpenses(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        specified_date_obj = datetime.datetime.strptime(data["specified_date"][:10], '%Y-%m-%d')
        expenses = Expense.objects.order_by('-date_created').filter(date_created__month=specified_date_obj.month)

        total_amount = expenses.aggregate(Sum('amount'))['amount__sum']
        if total_amount:
            total_amount = round(total_amount, 2)
        expenses_data = ExpenseSerializer(expenses, many=True).data
        return Response({'expenses': expenses_data, 'total_amount': total_amount})
    

class SubmitExpense(CreateAPIView):
    serializer_class = ExpenseSerializer


class DeleteExpense(DestroyAPIView):
    serializer_class = ExpenseSerializer    
    queryset = Expense.objects.all()