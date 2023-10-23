#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
from urllib import request
import requests
import sys
if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url+"users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url+"todos", params={"userId": u_id}).json()

    with open("{}.json".format(u_id), "w") as jsonfile:
        json.dump({u_id: [{"task": t.get("title"), "completed": t.get(
            "completed"), "username": username} for t in todos]}, jsonfile)
