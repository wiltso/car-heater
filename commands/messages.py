import os


def sendMessage(number, message):
    """\
    sendMessage: function to send a messages to a number 
    :param number: The phone number that the message will be sent to
    :type number: String 
    :param message: The message that will be sent
    :type group: message\
    """
    os.system('sudo gammu --sendsms TEXT %s -len 400 -text "%s"' % (number, message))
    return "Messages was sent", True
