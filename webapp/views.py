from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from django.views import View

from webapp.models import Employee, Equipment, Operation


class EmployeeListView(ListView):
    model = Employee
    template_name = 'webapp/employee.html'
    ordering = ['name']
    extra_context = {'title': 'Персонал'}


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'webapp/equipment.html'
    extra_context = {'title': 'Оборудование'}


class OperationListView(ListView):
    model = Operation
    template_name = 'webapp/operation.html'
    ordering = ['number']
    extra_context = {'title': 'Операции'}


class RoadMapView(View):
    def get(self, request):
        operations = Operation.objects.order_by('number')
        context = {'operations': operations, 'title': 'Маршрутная карта'}
        return render(request, context=context, template_name='webapp/roadmap.html')
