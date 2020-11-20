import re
import os
import json
import commands
from itertools import chain


def readMessages():
    text = ""
    numberFinder = re.compile('\+\d+')
    with open(commands.getPath() + "files/allMessages.txt") as f:
        text = f.read()

    # Removes the bottom part telling how many messages there are
    text = text.split("\n\n\n")[0]

    allMessages = text.split("\n\nLocation ")
    sorted_messages = []

    for holeMessage in allMessages:
        compliedMessage = {}
        holeMessage = holeMessage.split("\n")[2:]
        addCommand = True
        messageText = ""
        for line in holeMessage:
            if "Remote number" in line:
                compliedMessage["number"] = numberFinder.findall(line)[0]
            elif "Status" in line:
                line = line.split(": ")[1]
                if line == "Read":
                    addCommand = False
                else:
                    addCommand = True
            elif ":" in line or "" == line:
                pass
            else:
                messageText += line + "\n"

        if addCommand:
            compliedMessage["text"] = messageText
            sorted_messages.append(compliedMessage)

    return sorted_messages


def updateMessageFile():
    res = os.system("gammu getallsms > %sfiles/allMessages.txt" % (commands.getPath()))



def removeOldMessages():
    os.system("gammu deleteallsms 1")
    os.system("gammu deleteallsms 2")
    os.system("gammu deleteallsms 3")
    os.system("gammu deleteallsms 4")



def saveUnHandeldMessages(messages):
    oldMessages = commands.readData(readFile=commands.getPath() + "files/unHandeldMessages.json")
    if oldMessages:
        messages.extend(oldMessages)
    commands.writeData(messages, readFile=commands.getPath() + "files/unHandeldMessages.json")


def handelMessages(messages):
    successMessages = []
    unHandeldMessages = []
    for message in messages:
        if not "number" in message:
             continue
        splittedMessage = message["text"].split("\n")
        command = splittedMessage[0]
        kwargs = [var.split("& ") for var in splittedMessage[1:]]
        kwargs = iter(list(chain.from_iterable(kwargs)))
        print(messages)
        if message["number"] in commands.getAdminNumbers():
            kwargs = dict(zip(kwargs, kwargs))
            returnMessage, success = executeCommand(command, kwargs)
            successMessages.append([returnMessage, message["number"]])
            if not success:
                unHandeldMessages.append(message)

        elif (message["number"] in commands.getAuthenticatedNumbers() and
                command in commands.getAuthenticatedNumbersCommands()):
            kwargs = dict(zip(kwargs, kwargs))
            returnMessage, success = executeCommand(command, kwargs)
            successMessages.append([returnMessage, message["number"]])
            if not success:
                unHandeldMessages.append(message)

        else:
            unHandeldMessages.append(message)
    if unHandeldMessages:
        saveUnHandeldMessages(unHandeldMessages)
    for message, number in successMessages:
        commands.sendMessage(number, message)


def executeCommand(command, kwargs):
    function = getattr(commands, command, None)
    if function:
        try:
            return function(**kwargs)
        except Exception as e:
            raise e
            return "Failed error is: \"%s\" and the kwargs: \"%s\" " % (e, kwargs), False
    return "Function (%s) dose not exist" % (command), False
