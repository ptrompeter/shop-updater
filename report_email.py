#!/usr/bin/env python3

"""This script compiles names and weights from product description
files in a directory into a single paragraph, then generates a pdf report from it
with the current date."""

import datetime
import os
import sys

from run import parse_file
from reports import generate_report

def generate_title():
    date = datetime.datetime.now()
    title = "Processed Update on {}".format(date.strftime("%A, %B %d, %Y."))
    return title

def generate_paragraph(parsed_dict):
    """Return a formatted paragraph from a dictionary parsed by
    run.py.parse_file (with False passed to weight_int param)."""
    paragraph = "Name: {}<br/> Weight: {} <br/><br/>".format(parsed_dict["name"], parsed_dict["weight"])
    return paragraph

def controller(attachment=None, source="supplier-data/descriptions"):
    """Compile all descriptions from a folders into single report."""
    filenames = os.listdir(source)
    title = generate_title()
    paragraph = ""
    for file in filenames:
        dict = parse_file(file, source, False)
        print("dict:", dict)
        paragraph += generate_paragraph(dict)
        print("paragraph:", paragraph)
        print("Length:", len(paragraph))
    if attachment:
        generate_report(title, paragraph, attachment)
    else:
        generate_report(title, paragraph)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        controller(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        controller(sys.argv[1])
    else:
        controller()
