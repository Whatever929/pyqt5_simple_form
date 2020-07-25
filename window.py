from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QMenu, QStatusBar, QHBoxLayout, QVBoxLayout, QStatusBar
from PyQt5.QtCore import Qt
from form import Form
import PyQt5.QtGui as QtGui

class Window(QMainWindow):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.setWindowTitle("Register Form")
        self.setFixedSize(750, 750)
        self.move(0,0)
        self.add_menu()
        self.add_status_bar()
        self.add_central_widget()
    def add_menu(self):
        setting = self.menuBar().addMenu("&Setting")
        exit = self.menuBar().addMenu("&Exit")
        setting.addAction("Themes")
        setting.addAction("Font Size")
        exit.addAction("Exit")
    def add_status_bar(self):
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("Ready to go")
        self.setStatusBar(self.statusBar)
    # def change_status_bar(self, msg):
    #     self.statusBar.showMessage(msg)
    def create_title(self):
        label = QLabel("PyQT Register Form")
        label.setFont(QtGui.QFont('Arial', 20, QtGui.QFont.Bold))
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        widget = QWidget()
        widget.setLayout(layout)
        widget.setFixedSize(750, 75)
        return widget
    def add_central_widget(self):
        form = Form(self.statusBar)
        title = self.create_title()
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(title)
        central_layout.addWidget(form)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
