#!/usr/bin/python3
"""
Exports employee TODO list data to a CSV file structure.
"""
import csv
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

    filename = "{}.csv".format(user_id)

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_list:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])