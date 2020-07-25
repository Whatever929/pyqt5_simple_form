import pathlib

from debug.log import Log
logger = Log(__name__, pathlib.Path.cwd() / "debug" / "saveLog.txt")
count = 0

# Details is a tuple of form information, status is the main window's status bar.
def save_data(details: tuple, status):
    with open(pathlib.Path.cwd() / "record" / "data.txt", "a") as out:
        with open(pathlib.Path.cwd() / "record" / "counter.txt", "r") as counter:
            content = counter.read()
            global count
            count = eval(content)
            data = """
ID: {0}
Name: {1[0]}
Age: {1[1]}
Gender: {1[2]}
Identity: {1[3]}
Date of birth: {1[4]}
Nationality: {1[5]}
Program: {1[6]}
        """.format(count, details)
            out.write(data)
            status.showMessage("Registered successful with ID {}".format(count))
        with open(pathlib.Path.cwd() / "record" / "counter.txt", "w") as new_count:
            new_count.write(str(count + 1))
