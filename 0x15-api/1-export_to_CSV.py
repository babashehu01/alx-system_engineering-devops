#!/usr/bin/python3
"""Getting website data using API and save it as CSV"""
import requests
import sys


#!/usr/bin/python3
"""
Using a REST API, for a given employee ID and returns information
about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":

    id_user = int(sys.argv[1])

    req_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    req_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    csv_file = sys.argv[1] + '.csv'

    with open(csv_file, mode='w') as export_csv_file:
        file_to_export = csv.writer(
            export_csv_file, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_ALL)

        for i in req_user:
            if id_user == i.get('id'):
                USERNAME = i.get('username')

        for j in req_todos:
            USER_ID = j.get('userId')
            TASK_COMPLETED_STATUS = j.get('completed')
            TASK_TITLE = j.get('title')
            if id_user == j.get('userId'):
                file_to_export.writerow([
                     USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])


#    url = 'https://jsonplaceholder.typicode.com/'
#    user_id = int(sys.argv[1])
#
#    """Getting username"""
#    req = "{}users/{}".format(url, user_id)
#    user = requests.get(req)
#    user = user.json()
#    username = user['username']
#
#    """Getting tiltle and todo status"""
#    req = "{}todos?userId={}".format(url, user_id)
#    tasks = requests.get(req)
#    tasks = tasks.json()
#
#    for task in tasks:
#        print(f'"{user_id}","{username}","{task["completed"]}","{task["title"]}"')
