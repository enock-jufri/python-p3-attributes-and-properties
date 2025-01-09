#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        # Only set and validate name if it's explicitly provided
        if name is not None:
            self.name = name  # Uses the setter
        else:
            self._name = None

        # Only set and validate breed if it's explicitly provided
        if breed is not None:
            self.breed = breed  # Uses the setter
        else:
            self._breed = None

    def get_name(self):
        return getattr(self, "_name", None)  # Safe access with a default value

    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    name = property(get_name, set_name)

    def get_breed(self):
        return getattr(self, "_breed", None)  # Safe access with a default value

    def set_breed(self, breed):
        if breed:
            if breed.capitalize() in APPROVED_BREEDS:
                self._breed = breed.capitalize()
            else:
                print("Breed must be in list of approved breeds.")
                self._breed = None
        else:
            self._breed = None  # Allow empty or `None` without printing an error

    breed = property(get_breed, set_breed)
