from django.shortcuts import render

from rest_framework import viewsets
from .models import Department, Employee, Payroll, TimeAttendance, Benefit, PerformanceReview
from .serializers import DepartmentSerializer, EmployeeSerializer, PayrollSerializer, TimeAttendanceSerializer, BenefitSerializer, PerformanceReviewSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

class TimeAttendanceViewSet(viewsets.ModelViewSet):
    queryset = TimeAttendance.objects.all()
    serializer_class = TimeAttendanceSerializer

class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

