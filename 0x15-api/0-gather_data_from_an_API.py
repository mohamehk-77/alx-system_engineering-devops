#!/usr/bin/python3

"""
Fetches TODO list progress information for an employee using the JSONPlaceholder API.

Takes an employee ID as a command-line argument and displays the progress
in the following format:

Employee NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE 1 (with one tab and a space before the title)
    TASK_TITLE 2
    ... (other completed tasks)
"""

import requests
from sys import argv


def get_progress(employee_id):
    """
    Retrieves TODO list progress information for an employee from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee whose progress to retrieve.

    Returns:
        str: A formatted string containing the employee's name, total tasks,
             completed tasks, and a list of completed task titles.

    Raises:
        Exception: If an error occurs during API requests or data extraction.
    """

    base_url = "https://jsonplaceholder.typicode.com/users/"
    tasks_url = f"{base_url}{employee_id}/todos"

    try:
        # Fetch user data
        response = requests.get(base_url + employee_id)
        data = response.json()
        name = data.get("name")

        # Fetch TODO list
        response = requests.get(tasks_url)
        data = response.json()

        tasks = [task.get("title")
                 for task in data if task.get("completed") is True]
        completed_tasks = len(tasks)
        total_tasks = len(data)

        progress_string = (
            f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):\n"
        )

        for task in tasks:
            progress_string += f"\t {task}\n"

        return progress_string
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return ""


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
        progress_info = get_progress(employee_id)
        print(progress_info)
    except ValueError:
        print("Please provide a valid integer employee ID.")
