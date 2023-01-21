#!/usr/bin/python3
"""This script fetches a url
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    page = response.read()
print('Body reponse:')
print(f'\t- type: {type(page)}')
print(f'\t- content: {page}')
print(f"\t- utf8 content: {page.decode('UTF8')}")
