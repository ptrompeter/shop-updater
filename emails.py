#!/usr/bin/env python3

"""This script creates a sends an email confirming the updating of a service with new products."""

import email.message
import mimetypes
import os
import smtplib

default_subject = "Upload Completed - Online Fruit Store"
default_body = "All fruits are uploaded to our website successfully.  A detailed list is attached to this email."
def generate_email(recipient, sender="automation@example.com" subject=default_subject, body=default_body, attachment_path="/tmp/processed.pdf"):
    """Generate an email """
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    #Add attachment (pdf report)
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
        message.add_attachement(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attachment_filename)
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == "__main__":
    message = generate_email(*args)
    send_email(message)
