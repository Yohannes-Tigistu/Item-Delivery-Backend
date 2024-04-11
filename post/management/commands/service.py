from django.core.management.base import BaseCommand
from faker import Faker
from decimal import Decimal
from random import randint, choice
from datetime import timedelta
from django.utils import timezone
from user.models import serviceProviders, Profile
from post.models import City, Service, Path

class Command(BaseCommand):
    help = 'Generate fake data for cities, services, and paths'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        City.objects.all().delete()
        Service.objects.all().delete()
        Path.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Cleared existing data successfully'))

        # Generate 20 cities
        for _ in range(20):
            City.objects.create(name=fake.city())

        cities = City.objects.all()
        self.stdout.write(self.style.SUCCESS('Generated 20 cities successfully'))

        # Generate 70 services
        for _ in range(70):
            creator = serviceProviders.objects.order_by('?').first()
            content = fake.text()
            created_at = fake.date_time_this_year()
            price = Decimal(randint(10, 1000))  # Random price between 10 and 1000

            service = Service.objects.create(creator=creator, content=content, created_at=created_at, price=price)

            # Randomly add views
            profiles = Profile.objects.order_by('?')[:randint(1, 10)]
            service.views.add(*profiles)
        self.stdout.write(self.style.SUCCESS('Generated 70 services successfully'))

        # Generate 100 paths
        for _ in range(100):
            service = choice(Service.objects.all())
            origin = choice(cities)
            destination = choice(cities)
            updated_at = timezone.now()
            price = Decimal(randint(10, 500))  # Random price between 10 and 500
            departure_time = timezone.now() + timedelta(days=randint(-1, 1), hours=randint(-12, 12), minutes=randint(-30, 30))
            estimated_arrival_time = departure_time + timedelta(hours=randint(1, 24))

            Path.objects.create(service=service, origin=origin, destination=destination, updated_at=updated_at, price=price, departure_time=departure_time, estimated_arrival_time=estimated_arrival_time)

        self.stdout.write(self.style.SUCCESS('Generated 100 paths successfully'))
