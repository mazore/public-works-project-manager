from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import QSize
from .table import Table

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.setFixedSize(QSize(600, 400))

        layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(Table())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def keyPressEvent(self, key):
        if key.text() == 'q':
            quit()
