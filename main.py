#! /usr/bin/python
from messages import readMessages, updateMessageFile, handelMessages, removeOldMessages
import time

while True:
    updateMessageFile()
    newMessages = readMessages()
    handelMessages(newMessages)
    time.sleep(10)
