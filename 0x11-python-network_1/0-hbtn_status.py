#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        look = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(look)))
        print("\t- content: {}".format(look))
        print("\t- utf8 content: {}".format(look.decode('utf-8')))
