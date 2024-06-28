#!/usr/bin/python3
import csv
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

def export_to_csv(employee_id, employee_name, todos):
    """Export TODO list data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name, todos = fetch_employee_data(employee_id)
    export_to_csv(employee_id, employee_name, todos)
    print(f"Data exported to {employee_id}.csv")

