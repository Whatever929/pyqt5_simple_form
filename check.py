# This module checks if all the inputs are valid.

def check_input(details: tuple, status_bar):
    for i in details:
        if hasattr(i, "currentText"):
            pass
        elif i.text() == "":
            status_bar.showMessage("You have empty fields.")
            i.setStyleSheet("border: 1px solid red;")
            return False
        i.setStyleSheet("")
    # Age
    if details[1].text().isdigit():
        if 110 < int(details[1].text()) or int(details[1].text()) < 0:
            status_bar.showMessage("Your age is invalid.")
            return False
    else:
        status_bar.showMessage("Your age is invalid.")
        return False

    return True
