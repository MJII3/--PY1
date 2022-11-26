import csv
import json
from os import write

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:

 data = {}
 for row in reader:
     data.append({{column -> value}, ... , {column -> value}})
 print(data)

 with open('newinput.joson', 'w') as f:
     json.dumps(csv_to_list_dict(INPUT_FILE), indent=4)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
