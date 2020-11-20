from .special import getPath
import json


def readData(readFile=getPath() + "files/constants.json", permission="r+"):
    with open(readFile, permission) as f:
        return json.load(f)


def writeData(data, readFile=getPath() + "files/constants.json", permission="w"):
    with open(readFile, permission) as f:
        json.dump(data, f, indent=4, sort_keys=True)
