import commands
import os


def updateRepo():
    res = os.system("git checkout main")
    res =+ os.system("git pull")
    return res, True


def getHelp():
    """\
    getHelp: Gets all the information about the functions
    """
    return_string = ""
    for command in commands.__all__:
        help_text = getattr(getattr(commands, command, None), "__doc__", None)
        if help_text:
            return_string += str(help_text).replace("    ", "") + "\n\n"
    return return_string, True

