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

    # Fetch user data to get username
    user_res = requests.get("{}users/{}".format(url, user_id))
    username = user_res.json().get("username")

    # Fetch todo list items
    todos_res = requests.get("{}todos?userId={}".format(url, user_id))
    todos_list = todos_res.json()

    # Structure tasks into list of dictionaries
    tasks_data = []
    for task in todos_list:
        tasks_data.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Wrap inside the user ID string key
    json_payload = {user_id: tasks_data}
    filename = "{}.json".format(user_id)

    # Write dictionary payload to a JSON file
    with open(filename, mode='w') as json_file:
        json.dump(json_payload, json_file)