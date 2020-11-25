#!/usr/bin/env python3

"""This script uploads image files to a webserver using the requests module."""

import os
import requests
import sys


def get_list_of_jpegs(path):
    """Get a list of jpegs in a directory"""
    file_list = os.listdir(path)
    jpeg_list = [x for x in file_list if x[-4:]]
    return jpeg_list

def upload_file(path, file, url):
    """Access a file and post it via the requests module."""
    with open(os.join(path, file), 'rb') as f:
        r = requests.post(url, files={'file': f})

def manage_script(path, url):
    """Run the upload_file function for every file in a directory."""
    jpeg_list = get_list_of_jpegs(path)
    for item in jpeg_list:
        r = upload_file(path, item, url)
        print(r.status_code)
    # print(jpeg_list)
    # print(path)
    # print(url)

if __name__ == "__main__":
    manage_script(sys.argv[1], sys.argv[2])
