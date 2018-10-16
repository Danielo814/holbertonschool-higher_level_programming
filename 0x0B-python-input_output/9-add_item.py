#!/usr/bin/python3
"""
9-add_item module
"""

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
import sys
import json


filename = 'add_item.json'
try:
    new = load_from_json_file(filename)
except:
    new = []
finally:
    for i in range(1, len(sys.argv)):
        new.append(sys.argv[i])
    save_to_json_file(new, filename)
