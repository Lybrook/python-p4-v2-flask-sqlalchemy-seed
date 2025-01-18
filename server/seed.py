#!/usr/bin/env python3
#server/seed.py

from faker import Faker
from app import app
from models import db, Pet
import random

with app.app_context():

    rc = random.choice

    fake = Faker()

    Pet.query.delete()
    # Create an empty list
    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()