# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

# Import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")

# setup django environment
import django

django.setup()

# Import your models for use in your script
from db.models import *


# Index scan
myplace = Place.objects.all().filter(id=5)
print(f"{len(myplace)}")

# This is a sequential scan
allPlaces = Place.objects.all()
print(f"{len(allPlaces)}")

#Index only scan
placeCount = Place.objects.filter(id__lt = 1000).count()



