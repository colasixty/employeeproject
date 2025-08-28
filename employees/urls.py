from django.urls import path
from .views import AverageSalaryView, DepartmentSummaryView, AttendanceListView, LeaveListView

urlpatterns = [
    path('average-salary/', AverageSalaryView.as_view(), name='average-salary'),
    path('department-summary/', DepartmentSummaryView.as_view(), name='department-summary'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('leaves/', LeaveListView.as_view(), name='leave-list'),
]
