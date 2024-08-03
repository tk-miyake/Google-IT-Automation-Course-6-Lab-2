#!/usr/bin/env python3

import os
import requests

src_dir = "/data/feedback/"

for files in os.listdir(src_dir):
    with open(src_dir + files, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    key_lists = ["title", "name", "date", "feedback"]
    feedback_data = dict(zip(key_lists, lines))

    response = requests.post("http://<corpweb-external-IP>/feedback/", data=feedback_data)
    print("status_code", response.status_code)
