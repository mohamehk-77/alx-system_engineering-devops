#!/usr/bin/python3
"""A Python script using this REST API, for a given employee ID."""
import csv
from requests import get
from sys import argv


def cvsWrite(user):
    """Write to csv."""
    # get the Response from the API endpoint and convert to json format
    Response = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                   .format(user)).json()
    # get the employee name from the API endpoint and convert to json format
    employee_name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    # write the data to csv format and save to a file named USER_ID.csv
    employ_data = open('{}.csv'.format(user), 'w')
    # create the csv writer_object and write the data to the file in csv format
    writer_object = csv.writer(employ_data, quoting=csv.QUOTE_ALL)
    # write the data to the file in csv format
    for line in Response:
        lines = [line.get('userId'), employee_name,
                 line.get('completed'), line.get('title')]
        writer_object.writerow(lines)
    employ_data.close()


if __name__ == "__main__":
    cvsWrite(argv[1])
