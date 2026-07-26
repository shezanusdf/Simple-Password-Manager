import json
def load_records():
    try:
        with open("records.json","r") as file:
            try:
                return json.load(file)
            except:
                return {}
    except:
        return {}
    
def dump_records(passwords):
    with open("records.json","w") as file:
        json.dump(passwords, file, indent = 4)