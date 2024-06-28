import json
import requests

def fetch_users_and_tasks():
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    users = users_response.json()
    tasks = tasks_response.json()

    return users, tasks

def create_user_tasks_dict(users, tasks):
    user_tasks_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks_dict[user_id] = []

        for task in tasks:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks_dict[user_id].append(task_info)

    return user_tasks_dict

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def main():
    users, tasks = fetch_users_and_tasks()
    user_tasks_dict = create_user_tasks_dict(users, tasks)
    save_to_json(user_tasks_dict, "todo_all_employees.json")

if __name__ == "__main__":
    main()
