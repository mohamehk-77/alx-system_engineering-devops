#!/usr/bin/python3
"""A Python script using this REST API, for a given employee ID."""
import json
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
    list = []
    # write the data to a file named USER_ID.json in json format
    for line in Response:
        list.append({"task": line.get('title'),
                     "completed": line.get('completed'),
                     "username": employee_name})
    with open('{}.json'.format(user), 'w') as f:
        json.dump({user: list}, f)


if __name__ == "__main__":
    cvsWrite(argv[1])
