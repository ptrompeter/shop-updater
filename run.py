#!/usr/bin/env python3

"""This script reads text files from a directory, formats them into a JSON
object, and uploads them to a url."""

import os
import re
import requests
import sys

def parse_file(filename, path):
    """Turn a specifically formatted text file into a dictionary with image location."""
    dict = {}
    file_path = os.path.join(path, filename)
    with open(file_path, "r") as f:
        dict["name"], dict["weight"], dict["description"] = file_path.readlines()
        #file_dict["weight"] = file_path.readline()
        #file_dict["description"] = file_path.readline()
    match = re.match(r'^(\d+(\.\d)?)', dict["weight"])
    try:
        weight = int(match[1])
    except ValueError:
        weight = float(match[1])
        weight = int(weight)
    dict["weight"] = weight
    root, ext = os.path.spitext(filename)
    dict["image_name"] = root + ".jpeg"
    return dict

def upload_dict(dictionary, url):
    r = requests.post(url, json=dictionary)
    print(r.status_code)

def manage_script(path, url):
    for file in os.path.listdir(path):
        dict = parse_file(file, path)
        upload_dict(dict, url)

if __name__ = "__main__":
    manage_script(sys.argv[1], sys.argv[2])
