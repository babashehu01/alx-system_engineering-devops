#!/usr/bin/python3
"""Getting data from an API """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = int(sys.argv[1])

    """Getting the user NAME using ID"""
    user = '{}users/{}'.format(url, user_id)
    response = requests.get(user)
    to_obj = response.json()

    print("Employee {} is done with tasks ".format(to_obj['name']), end='')

    """Getting task done by employee"""
    todos = '{}todos?userId={}'.format(url, user_id)
    response = requests.get(todos)
    tasks = response.json()
    task_list = []
    for task in tasks:
        if task['completed'] is True:
            task_list.append(task)
    
    print("({}/{}):".format(len(task_list), len(tasks)))

    """Printing the title of each completed task"""
    for task in task_list:
        print("\t {}".format(task['title']))
