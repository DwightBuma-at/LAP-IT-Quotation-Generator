from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Employee, Quotation
import json

@csrf_exempt
def create_quotation(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		emp_id = data.get('emp_id')
		try:
			employee = Employee.objects.get(emp_id=emp_id)
		except Employee.DoesNotExist:
			return JsonResponse({'error': 'Employee not found'}, status=404)
		quotation = Quotation(employee=employee)
		quotation.save()
		return JsonResponse({'quotation_no': quotation.quotation_no})
	return JsonResponse({'error': 'Invalid request'}, status=400)
def quotation(request):
	# Render quotation.html as a Django template
	return render(request, 'quotation.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
	# Render index.html as a Django template so static tags work
	return render(request, 'index.html')

# Create your views here.
