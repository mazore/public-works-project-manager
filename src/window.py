from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import json
import sys
import os.path
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
            sys.exit()

    def load_data_from_db_file(self):
        """Flattened data list parsed from db including parsed dt and city_id"""
        if not os.path.exists('db.json'):
            self.data = []
            return

        data = []
        with open('db.json') as f:
            db = json.load(f)
        for city_id, projects in db.items():
            for project in projects:
                data.append({
                    **project,
                    'city_id': city_id,
                    'dt': parse_datetime(project['time'])
                })
        self.data = self.sort_data(data)

        if any(project.get('new') for project in self.data):
            self.clear_new_flags(db)

    @staticmethod
    def sort_data(data):
        # new_projects = [p for p in self.data if p.get('new')]
        new_projects, not_new_projects = [], []
        for project in data:
            (not_new_projects, new_projects)[project.get('new', False)].append(project)
        not_new_projects.sort(key=lambda project: project['dt'], reverse=True)
        return new_projects + not_new_projects

    def clear_new_flags(self, db):
        # Clear "new" flags in db file for next time
        print('clearing new flags')
        for projects in db.values():
            for project in projects:
                if 'new' in project:
                    del project['new']
        with open('db.json', 'w') as f:
            json.dump(db, f, indent=4)
