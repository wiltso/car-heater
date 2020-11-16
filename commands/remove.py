from .base import readData, writeData


def removeNumber(number, group="AUTHENTICATED_NUMBERS"):
    """\
    removeNumber: function to remove a phone number from a group 
    :param number: The phone number that will be removed from the group
    :type number: String 
    :param group: The group name the phone number should be removed from
    :type group: String\
    """
    data = readData()
    try:
        data[group].remove(number)
    except ValueError:
        return "Failed: group %s dose not exist" % (group), False
    except Exception as e:
        return "Failed: error messages %s" % (e), False
    writeData(data)
    return "Command successfully executed", True


def removeCommandFromGroup(command, group="AUTHENTICATED_NUMBERS_COMMANDS"):
    """\
    removeCommandFromGroup: function to remove a command from a group 
    :param number: The command name that will be remove from the group
    :type number: String 
    :param group: The group name the phone number should be remove from
    :type group: String\
    """
    data = readData()
    try:
        data[group].remove(command)
    except ValueError:
        return "Failed: group %s dose not exist" % (group), False
    except Exception as e:
        return "Failed: error messages %s" % (e), False
    writeData(data)
    return "Command successfully executed", True
