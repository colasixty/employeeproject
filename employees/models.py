from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('ENG', 'Engineering'),
        ('MKT', 'Marketing'),
        ('FIN', 'Finance'),
        ('SALES', 'Sales'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        return f"{self.employee} - {self.date}"


class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('SICK', 'Sick Leave'),
        ('VACATION', 'Vacation'),
        ('UNPAID', 'Unpaid Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"
