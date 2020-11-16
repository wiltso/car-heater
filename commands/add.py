from .base import readData, writeData


def addNumber(number, group="AUTHENTICATED_NUMBERS"):
    """\
    addNumber: function to add number a phone number to a group 
    :param number: The phone number that will be added to the group
    :type number: String 
    :param group: The group name the phone number should be added to
    :type group: String\
    """
    data = readData()
    try:
        if number in data[group]:
            return "Number already in the sustem", True
        data[group].append(number)
    except KeyError:
        return "Group dose not exist", False
    except Exception as e:
        return "Faild: error messages %s" % (e), False
    writeData(data)
    return "Command successfully executed", True


def addCommandToGroup(command, group="AUTHENTICATED_NUMBERS_COMMANDS"):
    """\
    addCommandToGroup: function to add a command to a group 
    :param command: The command name that will be added to the group
    :type command: String 
    :param group: The group name the phone number should be added to
    :type group: String\
    """
    data = readData()
    try:
        if command in data[group]:
            return "Command already in the system", True
        data[group].append(command)
    except KeyError:
        return "Group dose not exist", False
    except Exception as e:
        return "Failed: error messages %s" % (e), False
    writeData(data)
    return "Command successfully executed", True
