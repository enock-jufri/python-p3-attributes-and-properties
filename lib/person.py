#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        self.name = name  # Uses the setter (and name can be None)
        self.job = job    # Uses the setter
    
    # Getter for `name`
    def get_name(self):
        return getattr(self, "_name", None)
    
    # Setter for `name`
    def set_name(self, name):
        if name is not None and (isinstance(name, str) and 0 < len(name) <= 25):
            self._name = name.title()  # Apply title case
        elif name is not None:
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = None  # If name is not provided, leave it as None.

    name = property(get_name, set_name)  # Correct property definition

    # Getter for `job`
    def get_job(self):
        return getattr(self, "_job", None)
    
    # Setter for `job`
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job  # Set job
        else:
            print("Job must be in list of approved jobs.")
            self._job = None

    job = property(get_job, set_job)  # Correct property definition


# Example Usage
person = Person(job="Admin")  # Now `name` can be omitted
print(person.name)  # Output: None (since no name was provided)
print(person.job)   # Output: Admin
