import requests


def TODO_list_progress(employee_id):

    api_url = "https://jsonplaceholder.typicode.com"

    get_employee_name = requests.get(f"{api_url}/users/{employee_id}")
    if get_employee_name.status_code != 200:
        print("NOT FOUND!")
        return
    employee_name = get_employee_name.json().get('name')

    todos_total = requests.get(f"{api_url}/todos", params={'userID': employee_id})
    if todos_total.status_code != 200:
        print("Failed to get that TODO list bud.")
        return
    todos = todos_total.json()
    finished_tasks = [todos for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks({len(finished_tasks)}/{finished_tasks}):")
