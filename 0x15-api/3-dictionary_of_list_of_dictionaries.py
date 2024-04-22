#!/usr/bin/python3
""" Returns information about an employee's TODO list progress
Exports data in JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo_dict = {}

    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")

        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        task_list = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name
        } for todo in todos]

        todo_dict[user_id] = task_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_dict, jsonfile, indent=4)

