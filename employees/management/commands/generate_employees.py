from django.core.management.base import BaseCommand
from employees.models import Employee, Attendance, Leave
from faker import Faker
import random
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = 'Generate synthetic data for Employee, Attendance, and Leave'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = [d[0] for d in Employee.DEPARTMENT_CHOICES]
        leave_types = [l[0] for l in Leave.LEAVE_TYPE_CHOICES]

        # Clear old data
        Employee.objects.all().delete()
        Attendance.objects.all().delete()
        Leave.objects.all().delete()

        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                department=random.choice(departments),
                salary=round(random.uniform(30000, 150000), 2),
                date_joined=fake.date_between(start_date='-5y', end_date='-30d')
            )
            employees.append(emp)

        for emp in employees:
            for _ in range(random.randint(5, 15)):
                date = fake.date_between(start_date='-60d', end_date='today')
                check_in = fake.time_object(end_datetime=datetime.now())
                check_out = (datetime.combine(datetime.today(), check_in) + timedelta(hours=8)).time()
                Attendance.objects.create(
                    employee=emp,
                    date=date,
                    check_in=check_in,
                    check_out=check_out
                )

        for emp in employees:
            for _ in range(random.randint(1, 3)):
                start = fake.date_between(start_date='-100d', end_date='-5d')
                end = start + timedelta(days=random.randint(1, 5))
                Leave.objects.create(
                    employee=emp,
                    start_date=start,
                    end_date=end,
                    leave_type=random.choice(leave_types),
                    reason=fake.sentence()
                )

        self.stdout.write(self.style.SUCCESS('Synthetic data generated successfully.'))
