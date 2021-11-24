import json


class JsonParser(object):
    def __init__(self, fileName):
        self.fileName = fileName
        with open(self.fileName, "r") as file:
            self.file = json.load(file)
