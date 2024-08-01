#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv, exit

def fetch_data(url):
    """Fetch data from a given URL and return JSON response."""
    try:
        response = get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        exit(1)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetch todos and users data
    todos_data = fetch_data(todos_url)
    users_data = fetch_data(users_url)

    # Find the employee name
    employee = None
    for user in users_data:
        if user.get('id') == employee_id:
            employee = user.get('name')
            break

    if not employee:
        print(f"No employee found with ID {employee_id}")
        exit(1)

    # Count completed tasks and total tasks
    completed = 0
    total = 0
    tasks = []
    
    for todo in todos_data:
        if todo.get('userId') == employee_id:
            total += 1
            if todo.get('completed'):
                completed += 1
                tasks.append(todo.get('title'))

    # Print results
    print(f"Employee {employee} is done with tasks({completed}/{total}):")
    for task in tasks:
        print(f"\t {task}")

