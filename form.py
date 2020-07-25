# Third-party library
from PyQt5.QtWidgets import QFormLayout, QWidget, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QCheckBox, QComboBox, QDateEdit
from PyQt5.QtCore import Qt

# Application specific modules
from file.save import save_data
from check import check_input
from debug.log import Log

# Standard Libary
import pathlib

class Form(QWidget):
    def __init__(self, status_bar):
        super().__init__()
        self.status_bar = status_bar
        self.logger = Log(self.__class__.__name__, pathlib.Path.cwd() / 'log_result' / "outForm.log")
        self.open_ended_details = ("Name", "Age", "Identity_No")
        self.dropdown_details = ("Gender", "Nationality", "Program")
        self.date_details = ("Date_of_Birth", )
        self.ordered_details = ("Name", "Age", "Gender", "Date_of_Birth",
        "Identity_No", "Nationality", "Program")
        self.add_form()
    # Piecing everything together
    def add_form(self):
        layout = QVBoxLayout()
        layout.addWidget(self.add_form_list())
        layout.addWidget(self.term_condition_button())
        layout.addWidget(self.add_form_but())
        self.setLayout(layout)
    # Create form list and saving reference for each form.
    def add_form_list(self):
        form_list_widget = QWidget()
        form_list = QFormLayout()
        details = self.ordered_details
        for i in details:
            if i == "Gender":
                dropdown = self.create_dropdown(("Male", "Female", "Others"))
                setattr(self, i.lower(), dropdown)
                form_list.addRow(i, dropdown)
            elif i == "Nationality":
                dropdown = self.create_dropdown(("Malaysian",
                "Non-Malaysian: Asian",
                "Others"))
                setattr(self, i.lower(), dropdown)
                form_list.addRow(i, dropdown)
            elif i == "Program":
                dropdown = self.create_dropdown(("Computer Science", "Law",
                "Economics", "Culinary Art"))
                setattr(self, i.lower(), dropdown)
                form_list.addRow(i, dropdown)
            elif i == "Date_of_Birth":
                dropdown = QDateEdit(calendarPopup=True)
                setattr(self, i.lower(), dropdown)
                form_list.addRow(i, dropdown)
            else:
                setattr(self, i.lower(), QLineEdit())
                form_list.addRow(i, getattr(self, i.lower()))
        form_list_widget.setLayout(form_list)
        return form_list_widget
    def add_form_but(self):
        button = QWidget()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        help_but = QPushButton("Help")
        submit_but = QPushButton("Submit")
        submit_but.clicked.connect(self.submit)
        layout.addWidget(help_but)
        layout.addWidget(submit_but)
        button.setLayout(layout)
        return button
    def term_condition_button(self):
        widget = QWidget()
        layout = QHBoxLayout()
        checkbox = QCheckBox("By checking this, you agree to our Term and Condition.")
        layout.addWidget(checkbox)
        widget.setLayout(layout)
        widget.setFixedSize(750, 50)
        return widget
    def submit(self):
        details = [getattr(self, i.lower()) for i in self.open_ended_details]
        if check_input(details, self.status_bar):
            detail = (self.name.text(), self.age.text(),
            self.gender.currentText(), self.identity_no.text(),
            self.date_of_birth.date().toPyDate(), self.nationality.currentText(),
            self.program.currentText())
            save_data(detail, self.status_bar)
            self.clear_input()
    def clear_input(self):
        for i in self.open_ended_details:
            form_input = getattr(self, i.lower())
            form_input.setText("")
    def create_dropdown(self, options: tuple):
        dropdown = QComboBox(self)
        for i in options:
            dropdown.addItem(i)
        return dropdown
