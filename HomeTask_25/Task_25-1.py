import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My_app')
        layout = QHBoxLayout()
        button1 = QPushButton('Кнопка 1')
        button2 = QPushButton('Кнопка2')
        layout.addWidget(button1)
        layout.addWidget(button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

