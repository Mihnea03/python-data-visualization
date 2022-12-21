from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit
from PySide6.QtCore import Qt
import pandautil

def add_layout():
    name_label = QLabel("Enter name:")
    name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    name_label.setFixedHeight(20)
    name_input = QPlainTextEdit()
    name_input.setFixedHeight(30)
    
    name_button = QPushButton("See all users with given name")
    name_button.clicked.connect()
    
    date_button = QPushButton("See birthdates stats")   
    opinion_button = QPushButton("See Yes/No stats") 
    layout = QVBoxLayout()
    layout.addWidget(name_label)
    layout.addWidget(name_input)
    layout.addWidget(name_button)
    layout.addWidget(date_button)
    layout.addWidget(opinion_button)
    
    return layout

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.setWindowTitle("DV")
        widget = QWidget()
        widget.setLayout(add_layout())
        self.setCentralWidget(widget)
    
