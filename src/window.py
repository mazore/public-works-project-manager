from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from .table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Public Works Project Manager')
        self.resize(900, 700)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(Table())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def keyPressEvent(self, key):
        if key.text() == 'q':
            quit()
