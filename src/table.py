from PyQt6.QtWidgets import QTableView, QLabel, QHeaderView, QTableWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import json
from .dt_helpers import parse_datetime
from . import table_attributes

with open('db.json') as f:
    DATA_TEST = json.load(f)


class Table(QTableWidget):
    def __init__(self):
        super().__init__()

        self.data_setup()
        self.extra_setup()

    def data_setup(self):
        flattened_data = []
        for city_id, projects in DATA_TEST.items():
            for project in projects:
                flattened_data.append(dict(**project, city_id=city_id))

        self.setColumnCount(3)
        self.setRowCount(len(flattened_data))
        for i, project in enumerate(flattened_data):
            dt = parse_datetime(project['time'])
            self.setCellWidget(i, 0, table_attributes.Time(dt))
            self.setCellWidget(i, 1, QLabel(project['name']))
            self.setCellWidget(i, 2, table_attributes.Url(project['url']))

    def extra_setup(self):
        self.verticalHeader().hide()
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QTableView.SelectionMode.NoSelection)
        self.setVerticalScrollMode(QTableView.ScrollMode.ScrollPerPixel)

        self.setHorizontalHeaderLabels(['Time', 'Name', 'URL'])
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        header.setFont(font)
