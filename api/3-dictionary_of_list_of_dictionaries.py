#!/usr/bin/python3
import json
import requests

def gather_data_from_api():
    base_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(base_url + 'users').json()
    todos = requests.get(base_url + 'todos').json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [task for task in todos if task.get('userId') == user_id]
        tasks_list = [{"username": username, "task": task.get('title'), "completed": task.get('completed')} for task in user_tasks]
        data[user_id] = tasks_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    gather_data_from_api()

