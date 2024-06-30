import csv
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker

# Create a function that generates a random date between two dates
def random_date(start_date: datetime, end_date: datetime):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.date()

# Create a function that generates a random selection from a list
def random_selection(list):
    return random.choice(list)

# Create a function that generates a random integer between two numbers
def random_int(start, end):
    return random.randint(start, end)

# Create a function that generates a random name using Faker package
def random_name():
    fake = Faker()
    return fake.name()

# Create a function that generates a random number between two numbers
def random_number(start, end):
    return random.uniform(start, end)

def random_entry(id):
    # Create a list of possible streams
    streams = ['Stream 1', 'Stream 2', 'Stream 3', 'Stream 4', 'Stream 5']
    # Create a list of possible statuses
    statuses = ['Success', 'Failure']
    # Create a list of possible failure domains
    failure_domains = ['Cougar', 'Main UI', 'Algo', 'IMC', 'DGS', 'DART']
    # Create a list of possible binning
    binning = ['Binning 1', 'Binning 2', 'Binning 3', 'Binning 4', 'Binning 5']

    # Create a random date
    date = random_date(datetime(2021, 1, 1), datetime(2023, 12, 31))
    # Create a random stream
    stream = random_selection(streams)
    # Create a random build number
    build_number = random_int(1, 100)
    # Create a random status
    status = random_selection(statuses)
    # Create a random duration in seconds
    duration = round(random_number(3600, 4000),2)
    # Create a random initiator
    initiator = random_name()
    # Create a random binning
    binning = random_selection(binning)
    # Create a random failure domain
    failure_domain = random_selection(failure_domains)

    return [id, date, stream, build_number, status, duration, initiator, binning, failure_domain]

def main():
    # df = pd.DataFrame(columns=['Id', 'Date', 'Stream', 'Build Number', 'Status', 'Duration', 'Initiator', 'Binning', 'Failure Domain'])
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Date', 'Stream', 'Build Number', 'Status', 'Duration', 'Initiator', 'Binning', 'Failure Domain'])
        for i in range(1, 101):
            writer.writerow(random_entry(i))

if __name__ == '__main__':
    main()