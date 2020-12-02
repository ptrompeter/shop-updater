"""A background script to monitor system health"""

import psutil
import socket
import sys

from emails import send_email

def cpu_too_hot():
    print("CPU %:", psutil.cpu_percent(1))
    if psutil.cpu_percent(1) > 80:
        return "Error - CPU usage is over 80%"

def low_disk_pace():
    total, used, free, percent = psutil.disk_usage("/")
    print("disk %:", percent)
    if percent > 80:
        return "Error - Available disk space is less than 20%"

def low_memory():
    mem = psutil.virtual_memory()
    print("Mem Space:", mem[1] / (1024 ** 2))
    if mem[1] / (1024 ** 2) < 500:
        return "Error - Available memory is less than 500MB"

def localhost_broken():
    local_host = socket.gethostbyname('localhost')
    print("localhost:", local_host)
    if local_host != "127.0.0.1":
        return "Error - localhost cannot be resolved to 127.0.0.1"

def health_test():
    for func in [cpu_too_hot, low_disk_pace, low_memory, localhost_broken]:
        message = func()
        if message:
            return message

def health_email(recipient, subject):
    """Generate an email """
    message = email.message.EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content("Please check your system and resolve the issue as soon as possible.")

    return message

def controller(recipient):
    message = health_test()
    if message:
        email = health_email(recipient, message)
        send_email(email)

if __name__ == "__main__":
    recipient = "{}@example.com".format(sys.args[1])
    controller(recipient)
