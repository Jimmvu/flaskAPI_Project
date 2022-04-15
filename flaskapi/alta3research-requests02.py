#!/usr/bin/env python3
import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/json"

resp = requests.get(URL).json()

print("The answers to the questions is: ")
print(f"{resp[0]['question']}: {resp[0]['answer']}")
print(f"{resp[1]['question']}: {resp[1]['answer']}")
print(f"{resp[2]['question']}: {resp[2]['answer']}")
