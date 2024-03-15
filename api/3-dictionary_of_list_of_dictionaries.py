#!/usr/bin/python3
""" File for pulling from APIs. """
import csv
import json
import requests
import sys

def TODO_list_all_json():
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users"
    todos_url = f"{api_url}/todos"
    users_data = requests.get(users_url).json()
    every_single_task = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        todos = requests.get(todos_url, params={'userId': user_id}).json()

        every_single_task[user_id] = [{
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in todos]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(every_single_task, file)


if __name__ == "__main__":
    TODO_list_all_json()
