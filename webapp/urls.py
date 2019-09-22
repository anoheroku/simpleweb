from django.urls import path

from webapp.views import EmployeeListView, EquipmentListView, OperationListView, RoadMapView

app_name = 'webapp'


urlpatterns = [
    path('', EmployeeListView.as_view(), name='root'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('equipment/', EquipmentListView.as_view(), name='equipment'),
    path('opertaions/', OperationListView.as_view(), name='operations'),
    path('roadmap/', RoadMapView.as_view(), name='roadmap')
]
