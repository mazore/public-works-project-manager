from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from .row import Row


class Table(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setWidget(widget)

        for i in range(150):
            layout.addWidget(Row(i))
