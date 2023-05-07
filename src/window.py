from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import json
from .controls import Controls
from .dt_helpers import parse_datetime
from .table import Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Public Works Project Manager')
        self.resize(900, 700)
        self.setMinimumSize(400, 300)

        self.load_data_from_db_file()
        self.controls = Controls(self)
        self.table = Table(self)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.controls)
        layout.addWidget(self.table)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def keyPressEvent(self, key):
        if key.text() == 'q':
            quit()

    def load_data_from_db_file(self):
        """Flattened data list parsed from db including parsed dt and city_id"""
        self.data = []
        with open('db.json') as f:
            db = json.load(f)
        for city_id, projects in db.items():
            for project in projects:
                self.data.append({
                    **project,
                    'city_id': city_id,
                    'dt': parse_datetime(project['time'])
                })
        self.data.sort(key=lambda project: project['dt'], reverse=True)
