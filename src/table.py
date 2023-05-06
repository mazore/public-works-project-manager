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
                flattened_data.append({
                    **project,
                    'city_id': city_id,
                    'dt': parse_datetime(project['time'])
                })
        flattened_data.sort(key=lambda project: project['dt'], reverse=True)

        self.setColumnCount(5)
        self.setRowCount(len(flattened_data))
        for i, project in enumerate(flattened_data):
            self.setCellWidget(i, 0, table_attributes.City(project))
            self.setCellWidget(i, 1, table_attributes.Date(project))
            self.setCellWidget(i, 2, table_attributes.Time(project))
            self.setCellWidget(i, 3, table_attributes.Name(project))
            self.setCellWidget(i, 4, table_attributes.Url(project))

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
