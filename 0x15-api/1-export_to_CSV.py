#!/usr/bin/python3
"""Getting website data using API and save it as CSV"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = int(sys.argv[1])

    """Getting username"""
    req = "{}users/{}".format(url, user_id)
    user = requests.get(req)
    user = user.json()
    username = user['username']

    """Getting tiltle and todo status"""
    req = "{}todos?userId={}".format(url, user_id)
    tasks = requests.get(req)
    tasks = tasks.json()

    for task in tasks:
        print(f'"{user_id}","{username}","{task["completed"]}","{task["title"]}"')
