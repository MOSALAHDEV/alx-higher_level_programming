#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    posted_data = b"email=" + email.encode("utf-8")
    request = urllib.request.Request(url, data=posted_data, method="POST")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
