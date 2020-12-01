#!/usr/bin/env python3

"""This script generates a pdf report from a text file using reportlab."""

import os

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
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])
