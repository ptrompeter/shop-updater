#!/usr/bin/env python3

"""This script generates a pdf report from a text file using reportlab."""

import datetime
import os
import requests
import sys

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from run import parse_file

def generate_report(title, paragraph, attachment="/tmp/processed.pdf"):
    """Return a reportlabs report given a formated title string and paragraph."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    print("report_title:", report_title)
    print("report_info:", report_info)
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])

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
