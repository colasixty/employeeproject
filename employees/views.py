from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Attendance, Leave
from django.db.models import Avg, Count
from rest_framework import generics
from .serializers import EmployeeSerializer, AttendanceSerializer, LeaveSerializer

class AverageSalaryView(APIView):
    def get(self, request):
        avg_salary = Employee.objects.aggregate(avg=Avg('salary'))
        return Response({'average_salary': round(avg_salary['avg'], 2)})

class DepartmentSummaryView(APIView):
    def get(self, request):
        summary = Employee.objects.values('department').annotate(count=Count('id'))
        return Response(summary)

class AttendanceListView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class LeaveListView(generics.ListAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer