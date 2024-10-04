from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.utils import IntegrityError
from home.models import *
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populates the database with fake employees.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', type=int, help='Indicates the number of employees to be created.'
        )

    def handle(self, *args, **kwargs):
        fake = Faker()
        number = kwargs.get('number') or 10  # Default to creating 10 employees

        # Ensure there are some positions in the database
        positions = Position.objects.all()
        if not positions.exists():
            positions_list = ['Manager', 'Engineer', 'Technician', 'Farmer', 'Supervisor']
            for pos_name in positions_list:
                Position.objects.create(name=pos_name)
            positions = Position.objects.all()
            self.stdout.write(self.style.SUCCESS('Created default positions.'))

        departments_list = ['Human Resources', 'Finance', 'Engineering', 'Sales', 'Marketing']

        created_count = 0
        for _ in range(number):
            name = fake.name()
            national_id = fake.unique.random_int(min=1000000000000, max=9999999999999)
            email = fake.unique.email()
            department = random.choice(departments_list)
            position = random.choice(positions)
            date_of_hire = fake.date_between(start_date='-5y', end_date='today')
            tag_id = fake.unique.lexify(text='??????????')
            phone_number = fake.phone_number()
            address = fake.address()
            day_salary = random.randint(5000, 50000)

            try:
                Employee.objects.create(
                    name=name,
                    national_id=national_id,
                    email=email,
                    department=department,
                    position=position,
                    date_of_hire=date_of_hire,
                    tag_id=tag_id,
                    phone_number=phone_number,
                    address=address,
                    day_salary=day_salary
                )
                created_count += 1
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(f'Error creating employee {name}: {e}'))
                continue

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} fake employees.'))
