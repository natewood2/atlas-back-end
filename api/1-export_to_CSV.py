#!/usr/bin/python3
""" File for pulling from APIs. """
import csv
import requests
import sys


def TODO_list_csv(employee_id):

    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users/{employee_id}"
    todos_url = f"{api_url}/todos"

    user_data = requests.get(users_url).json()
    username = user_data.get('username')

    todos = requests.get(todos_url, params={'userId': employee_id}).json()
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username,
                             todo['completed'], todo['title']])

    print("Well that worked fine...")


if __name__ == "__main__":

    TODO_list_csv(int(sys.argv[1]))
