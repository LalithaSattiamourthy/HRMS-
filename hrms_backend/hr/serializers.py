from rest_framework import serializers
from .models import Department, Employee, Payroll, TimeAttendance, Benefit, PerformanceReview

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PayrollSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 
    class Meta:
        model = Payroll
        fields = '__all__'

class TimeAttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 
    class Meta:
        model = TimeAttendance
        fields = '__all__'

class BenefitSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 
    class Meta:
        model = Benefit
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer() 
    class Meta:
        model = PerformanceReview
        fields = '__all__'
