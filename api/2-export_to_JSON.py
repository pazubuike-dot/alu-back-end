#!/usr/bin/python3
"""
Exports employee TODO list data to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_res = requests.get("{}users/{}".format(url, user_id))
    username = user_res.json().get("username")

    todos_res = requests.get("{}todos?userId={}".format(url, user_id))
    todos_list = todos_res.json()

    tasks_data = []
    for task in todos_list:
        tasks_data.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_payload = {user_id: tasks_data}
    filename = "{}.json".format(user_id)

    with open(filename, mode='w') as json_file:
        json.dump(json_payload, json_file)