#!/bin/python3

'''
Sample implementation of a donor database using classes
'''

class Person:
    '''
    Attributes common to any person
    '''
    def __init__(self, donor_id, name, last_name):
        self.donor_id = donor_id
        self.name = name
        self.last_name = last_name

class Donation:
    '''
    Attributes for a donation
    can be easily extended to support more complex
    properties
    '''
    def __init__(self, amount):
        self.amount = amount

class Donor(Person):
    '''
    Attributes for a person who is also a donor
    '''
    def __init__(self, donor_id, name, last_name):
        self.donations = []
        super().__init__(donor_id, name, last_name)

class DonorDB():
    '''
    A collection of donors
    '''
    def __init__(self):
        self.all_donors = {}

def add_donor(donor_collection):
    '''
    Creates a new donor and adds it to collection
    '''
    donor_id = input("Enter donor ID: ")
    name = input("Enter donor's name: ")
    last_name = input("Enter donor's lastname: ")
    new_donor = Donor(donor_id, name, last_name)
    if donor_id not in donor_collection.all_donors:
        donor_collection.all_donors[donor_id] = new_donor
    else:
        print("ERROR: Donor ID already exists")

def add_donation(donor_collection):
    '''
    Creates a new donation and adds it to a donor
    '''
    donor_id = input("Enter donor ID: ")
    if donor_id not in donor_collection.all_donors:
        print("ERROR: Donor ID does not exist")
        return
    donation_amount = int(input("Enter the donation amount: "))
    new_donation = Donation(donation_amount)
    donor_collection.all_donors[donor_id].donations.append(new_donation)

def print_db(donor_collection):
    '''
    Prints all donors / donations in a collection
    '''
    for donor_info in donor_collection.all_donors.values():
        print(f"Donor ID: {donor_info.donor_id}")
        print(f"Donor: {donor_info.name} {donor_info.last_name}")
        for donation_info in donor_info.donations:
            print(f"Donation: {donation_info.amount}")