#!/usr/bin/python3
""" File for pulling from APIs. """
import csv
import json
import requests
import sys


def TODO_list_json(employee_id):

    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users/{employee_id}"
    todos_url = f"{api_url}/todos"
    user_data = requests.get(users_url).json()
    username = user_data.get('username')

    params = {'userId': employee_id}
    todos_response = requests.get(todos_url, params=params)
    todos = todos_response.json()

    data = [{
        "task": todo['title'],
        "completed": todo['completed'],
        "username": username
    } for todo in todos]

    formatted_task = {str(employee_id): data}

    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as file:
        json.dump(formatted_task, file)
    print(f"Data for employee_id {employee_id} witten to {file_name}.")


if __name__ == "__main__":

    TODO_list_json(int(sys.argv[1]))
