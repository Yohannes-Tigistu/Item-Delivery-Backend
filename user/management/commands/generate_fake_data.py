from django.core.management.base import BaseCommand
from user.models import Profile, serviceProviders, User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate 50 users
        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            username = email  # You can change this if you want
            password = 'password'  # You can generate random passwords if needed
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

            # Generate profile for each user
            profile = Profile.objects.create(user=user, bio=fake.text(), phone_number=fake.phone_number(), profile_pic=fake.image_url())

            # Randomly assign 25 users as service providers
            if random.random() < 0.5:  # Adjust this probability as needed
                id_front = fake.image_url()
                id_back = fake.image_url()
                fayda_number = fake.random_number(digits=10)
                id_verified = fake.boolean()
                bank_account1 = fake.random_number(digits=10) if random.random() < 0.5 else ''
                bank_account2 = fake.random_number(digits=10) if random.random() < 0.5 else ''
                grand_father_name = fake.name() if random.random() < 0.5 else ''

                service_provider = serviceProviders.objects.create(profile=profile, id_front=id_front, id_back=id_back, fayda_number=fayda_number, id_verified=id_verified, bank_account1=bank_account1, bank_account2=bank_account2, grand_father_name=grand_father_name)

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully'))
