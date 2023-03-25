import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Описание')
        fileMenu = menubar.addMenu('&Инструкция')
        fileMenu = menubar.addMenu('&Описание')


        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
