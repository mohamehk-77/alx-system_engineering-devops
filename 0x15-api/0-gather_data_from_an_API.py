#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID."""
import requests
from sys import argv


def display_tasks():
    """Python script that fetches data for a given employee ID."""
    # link to fetch data from the API
    link = "https://jsonplaceholder.typicode.com/users/"

    # get the data from
    response = requests.get(link + argv[1])

    # convert the data to json format
    data = response.json()

    # get the name of the employee
    name = data.get("name")
    print("Employee {} is done with tasks".format(name), end="")

    # get the total number of tasks of the employee
    response = requests.get(link + argv[1] + "/todos")

    # convert the data to json format
    data = response.json()

    # get the completed tasks and the total number of them
    tasks = []
    for task in data:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("({}/{}):".format(len(tasks), len(data)))

    # print the completed tasks of the employee
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    display_tasks()
