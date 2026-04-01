import json


def saving(lst):
    l = lst[:]
    with open('to-do_info.json', 'w') as file:
        json.dump(l, file, indent=4)

def loading():
    try:
        with open('to-do_info.json', 'r') as file:
            loaded_data = json.load(file)
            return loaded_data
    except:
        return list()
