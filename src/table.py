from PyQt6.QtWidgets import QTableView, QHeaderView, QTableWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from . import table_attributes


class Table(QTableWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.setup()

    def setup(self):
        self.data_setup()
        self.extra_setup()

    def data_setup(self):
        self.clearContents()
        self.setColumnCount(len(table_attributes.attribute_types))
        self.setRowCount(len(self.window.data))
        for row, project in enumerate(self.window.data):
            for column, attr_type in enumerate(table_attributes.attribute_types):
                self.setCellWidget(row, column, attr_type(project))

    def extra_setup(self):
        self.verticalHeader().hide()
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QTableView.SelectionMode.NoSelection)
        self.setVerticalScrollMode(QTableView.ScrollMode.ScrollPerPixel)

        self.setHorizontalHeaderLabels(['⭐', 'City', 'Date', 'Time', 'Description', 'URL'])
        header = self.horizontalHeader()

        header.setSectionsClickable(False)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        header.setFont(font)

        header.setMinimumSectionSize(38)
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.resizeSection(0, 38)
        header.resizeSection(1, 150)
