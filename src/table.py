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
        self.setColumnCount(5)
        self.setRowCount(len(self.window.data))
        for i, project in enumerate(self.window.data):
            self.setCellWidget(i, 0, table_attributes.City(project))
            self.setCellWidget(i, 1, table_attributes.Date(project))
            self.setCellWidget(i, 2, table_attributes.Time(project))
            self.setCellWidget(i, 3, table_attributes.Name(project))
            self.setCellWidget(i, 4, table_attributes.Url(project))
            if project.get('new'):
                print('new project:', project['name'])

    def extra_setup(self):
        self.verticalHeader().hide()
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QTableView.SelectionMode.NoSelection)
        self.setVerticalScrollMode(QTableView.ScrollMode.ScrollPerPixel)

        self.setHorizontalHeaderLabels(['City', 'Date', 'Time', 'Description', 'URL'])
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        header.resizeSection(0, 150)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        # header.setSectionsClickable(False)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        header.setFont(font)
