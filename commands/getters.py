from .base import readData, writeData


def getAdminNumbers():
    data = readData()
    return data["ADMIN_NUMBERS"]


def getAuthenticatedNumbers():
    data = readData()
    return data["AUTHENTICATED_NUMBERS"]


def getAuthenticatedNumbersCommands():
    data = readData()
    return data["AUTHENTICATED_NUMBERS_COMMANDS"]

def getUnhandeldMessages():
    """\
    getUnhandeldMessages: Gets all the unhandeld messages and deletes them from the logs\
    """
    data = readData(readFile="unHandeldMessages.json")
    message = ""
    if not data:
        return "There are no unhandeld messages", True
    for dataMessage in data:
        message += str("Number: %s\nMessage: %s\n\n\n" % (dataMessage["number"], dataMessage["text"]))
    writeData(None, readFile="unHandeldMessages.json")
    return message, True

