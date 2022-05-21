import json


def GetDictFromJsonFile(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
