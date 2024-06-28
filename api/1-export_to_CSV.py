import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the employee data
    user_url = f"{base_url}/users/{employee_id}"
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print(f"Error fetching user data: {response_user.status_code}")
        return
    
    user_data = response_user.json()
    employee_name = user_data.get('username')

    # Fetch the TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print(f"Error fetching todos data: {response_todos.status_code}")
        return

    todos_data = response_todos.json()
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Save to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id, employee_name, todo.get('completed'), todo.get('title')])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
