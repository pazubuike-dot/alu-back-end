#!/usr/bin/python3
"""
Exports ALL employees' TODO list records into a single consolidated JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_res = requests.get("{}users".format(url))
    users_list = users_res.json()

    all_data = {}

    # Iterate through every user to fetch their respective tasks
    for user in users_list:
        user_id = str(user.get("id"))
        username = user.get("username")

        todos_res = requests.get("{}todos?userId={}".format(url, user_id))
        todos_list = todos_res.json()

        tasks_list = []
        for task in todos_list:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_data[user_id] = tasks_list

    # Output everything to the unified file
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_data, json_file)