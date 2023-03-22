from django.shortcuts import render
from .apps import FinancesConfig
from django.http import JsonResponse
from django.views import View
import json
from .models import Expense
from .serializers import ExpenseSerializer


app_name = FinancesConfig.name

# def index(request):
#     return render(request, 'finances/index.html')


class Index(View):
    template_name = 'finances/index.html'

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.all().order_by('-date_created')
        context = {
            'expenses': expenses
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        # print(data)
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            expense = serializer.save()
            # return JsonResponse({'success': True, 'expense_id': expense.id})
        else:
            return JsonResponse(serializer.errors, status=400)
        expenses = Expense.objects.all().order_by('-date_created')
        expenses_data = ExpenseSerializer(expenses, many=True).data
        return JsonResponse({'new_response': serializer.data, 'expenses': expenses_data})