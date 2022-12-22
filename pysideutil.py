from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit
from PySide6.QtCore import Qt
import pandautil

def add_layout():
    def search_by_name():
        pandautil.search_by_name(name_input.toPlainText())
        
    def search_by_date():
        pandautil.search_by_age()
    
    def search_by_opinion():
        pandautil.search_by_opinion()
        
    name_label = QLabel("Enter name:")
    name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    name_label.setFixedHeight(20)
    name_input = QPlainTextEdit()
    name_input.setFixedHeight(30)
    name_input.setMaximumBlockCount(1)
    
    name_button = QPushButton("See all users with given name")
    name_button.clicked.connect(search_by_name)
    
    date_button = QPushButton("See birthdates stats")   
    date_button.clicked.connect(search_by_date)
    
    opinion_button = QPushButton("See Yes/No stats") 
    opinion_button.clicked.connect(search_by_opinion)
    
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
    
