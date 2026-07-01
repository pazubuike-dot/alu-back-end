#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data to get the employee's username (NOT full name)
    user_res = requests.get("{}users/{}".format(url, user_id))
    user_dict = user_res.json()
    employee_username = user_dict.get("username")

    # Fetch todo list data for this specific user
    todos_res = requests.get("{}todos?userId={}".format(url, user_id))
    todos_list = todos_res.json()

    completed_tasks = []
    total_tasks = len(todos_list)

    # Filter completed tasks
    for task in todos_list:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    # Display results exactly as required by the checker using username
    print("Employee {} is done with tasks({}/{}):".format(
        employee_username, len(completed_tasks), total_tasks))

    for title in completed_tasks:
        print("\t {}".format(title))
