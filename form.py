# Third-party library
from PyQt5.QtWidgets import QFormLayout, QWidget, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QCheckBox, QComboBox
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
        self.add_form()
        self.logger = Log(self.__class__.__name__, pathlib.Path.cwd() / 'log_result' / "outForm.log")
    # Piecing everything together
    def add_form(self):
        layout = QVBoxLayout()
        layout.addWidget(self.add_form_list())
        layout.addWidget(self.term_condition())
        layout.addWidget(self.add_form_but())
        self.setLayout(layout)
    # Create form list and saving reference for each form.
    def add_form_list(self):
        form_list_widget = QWidget()
        form_list = QFormLayout()
        details = ["Name", "Age", "Gender", "Identity_No", "Date_of_Birth", "Nationality", "Program"]
        for i in details:
            if i == "Gender":
                dropdown = QComboBox(self)
                setattr(self, i.lower(), dropdown)
                dropdown.addItem("Male")
                dropdown.addItem("Female")
                dropdown.addItem("Others")
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
    def term_condition(self):
        widget = QWidget()
        layout = QHBoxLayout()
        checkbox = QCheckBox("By checking this, you agree to our Term and Condition.")
        layout.addWidget(checkbox)
        widget.setLayout(layout)
        widget.setFixedSize(750, 50)
        return widget
    def submit(self):
        detail = (self.name, self.age, self.gender, self.identity_no, self.date_of_birth, self.nationality, self.program)
        if check_input(detail, self.status_bar):
            detail = (self.name.text(), self.age.text(), self.gender.currentText(), self.identity_no.text(), self.date_of_birth.text(), self.nationality.text(), self.program.text())
            save_data(detail, self.status_bar)
            self.clear_input()
    def clear_input(self):
        details = ["Name", "Age", "Gender", "Identity_No", "Date_of_Birth", "Nationality", "Program"]
        for i in details:
            form_input = getattr(self, i.lower())
            form_input.setText("")
