import json

with open("test_cases.json", "r") as f:
    reader = json.load(f)

print(reader)
