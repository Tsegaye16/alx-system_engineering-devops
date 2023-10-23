#!/usr/bin/python3
# Python script to export data in the CSV forma.
import csv
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(u_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": u_id}).json()

    with open("{}.csv".format(u_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
