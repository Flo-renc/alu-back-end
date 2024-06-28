#!/usr/bin/python3
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee name and TODO list from JSONPlaceholder API."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = user_response.get("name")
    total_tasks = len(todos_response)
    completed_tasks = [task for task in todos_response if task.get("completed")]

    return employee_name, completed_tasks, total_tasks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, completed_tasks, total_tasks = fetch_employee_data(employee_id)
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
