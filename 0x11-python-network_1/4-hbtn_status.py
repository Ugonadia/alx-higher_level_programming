#!/usr/bin/python3
""" Module to fetch https://alx-intranet.hbtn.io/status
    with requests module
"""

import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(response), response))
