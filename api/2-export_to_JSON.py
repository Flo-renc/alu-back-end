#!/usr/bin/python3
import json
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee name and TODO list from JSONPlaceholder API."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = user_response.get("username")
    return employee_name, todos_response

def export_to_json(employee_id, employee_name, todos):
    """Export TODO list data to a JSON file."""
    filename = f"{employee_id}.json"
    tasks = [{"task": task.get("title"), "completed": task.get("completed"), "username": employee_name} for task in todos]
    data = {str(employee_id): tasks}

    with open(filename, mode='w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todos = fetch_employee_data(employee_id)
    export_to_json(employee_id, employee_name, todos)
    print(f"Data exported to {employee_id}.json")

