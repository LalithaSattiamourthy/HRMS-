# Create your models here.
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    join_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    performance_notes = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.employee} - {self.month}'

class TimeAttendance(models.Model):
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    overtime = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.employee} - {self.date}'

class Benefit(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    benefit_name = models.CharField(max_length=100)
    benefit_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.employee} - {self.benefit_name}'

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    review_text = models.TextField()
    goals = models.TextField()
    feedback = models.TextField()

    def __str__(self):
        return f'{self.employee} - {self.review_date}'
