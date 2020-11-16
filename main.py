from messages import readMessages, updateMessageFile, handelMessages
import time


while True:
    updateMessageFile()
    newMessages = readMessages()
    handelMessages(newMessages)
    time.sleep(10)
