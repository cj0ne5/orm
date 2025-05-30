############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

from faker import Faker

myfake = Faker()

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

"""
In case you need to start over. 
Note- this will delete any other tables on the public schema.
Alternatively, you could drop django's tables one-by-one

Login to psql and run these commands in order:

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres, public;

... then migrate again, and re-create your superuser
"""
'''
# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')
'''


#Place.objects.filter(name="Leonard LLC").count()  # Indexed query
Place.objects.filter(name__iexact="Leonard LLC").count()