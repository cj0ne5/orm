import sys
import os
import time
import random
from faker import Faker
from django.db import transaction


# Django setup stuff
# Note: Don't re-order these lines or weird stuff will happen
sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
import django
django.setup()
from db.models import *

####
#  Part 1: Generate lots of fake data
#
#   The faker code that we wrote before was pretty inefficient
#   This code is similar, but has some tweaks that make it way faster
#
####
myfake = Faker()


# Function to create random latitude and longitude within DC area
def random_latitude():
    return round(random.uniform(38.5, 39.5), 6)


def random_longitude():
    return round(random.uniform(-77.5, -76.5), 6)


places = []
owners = list(User.objects.all())

for _ in range(100):  # CHANGE THIS VALUE to test different table sizes
    places.append(
        #TODO: Replace this with the code that you wrote for Faker
        Place(
            name=myfake.company(),
            lat=random_latitude(),
            long=random_longitude(),
            owner=random.choice(owners),
        )
    )

with transaction.atomic():
    Place.objects.bulk_create(places, batch_size=500)  # Adjust batch_size as needed


####
#  Part 2: Run both versions of the query a bunch of times,
#   and print a summary
####


def test_query_exact():
    start = time.perf_counter()
    Place.objects.filter(name="Leonard LLC").count()  # Indexed query
    end = time.perf_counter()
    return end - start


def test_query_iexact():
    start = time.perf_counter()
    Place.objects.filter(name__iexact="Leonard LLC").count()  # Will trigger UPPER()
    end = time.perf_counter()
    return end - start


exact_times = []
iexact_times = []

for _ in range(50): # Change this value to change sample size
    exact_times.append(test_query_exact())
    iexact_times.append(test_query_iexact())

num_records = Place.objects.all().count()
avg_exact = round(sum(exact_times) / len(exact_times), 3)
avg_iexact = round(sum(iexact_times) / len(iexact_times), 3)


print(f"With {num_records} records in the table:")
print(f"\t- average time for query that uses index: {avg_exact} seconds")
print(f"\t- average time for query that does not use index: {avg_iexact} seconds")
