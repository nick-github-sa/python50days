import json

names = {'name': 'Carol','sex': 'female','age': 55}

def save_json(names):
    with open("json_file", "w") as file:
        json.dump(names, file, indent=4)

def read_json():
    with open('json_file', 'r') as file:
        data = json.load(file)
        print(data)

save_json(names)
read_json()







