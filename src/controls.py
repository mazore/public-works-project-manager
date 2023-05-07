from PyQt6.QtWidgets import QWidget, QPushButton, QProgressBar, QHBoxLayout
import json
import os.path
from .api import API
from .city_data import CITY_ID_NAME_MAP


class Controls(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        layout = QHBoxLayout()
        self.setLayout(layout)

        refresh = QPushButton('Refresh')
        refresh.clicked.connect(self.refresh)
        layout.addWidget(refresh)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        layout.addStretch()

    def refresh(self):
        first_refresh = False
        if os.path.exists('db.json'):
            with open('db.json') as f:
                db = json.load(f)
        else:
            first_refresh = True
            db = {}

        new_db = self.get_new_db(db, first_refresh)

        with open('db.json', 'w') as f:
            json.dump(new_db, f, indent=4)

        self.window.load_data_from_db_file()
        self.window.table.setup()

    def get_new_db(self, old_db, first_refresh):
        new_db = {}

        i = 0
        for city_id, name in CITY_ID_NAME_MAP.items():
            i += 1
            print(f'{i}/{len(CITY_ID_NAME_MAP)}: {name}')
            self.progress_bar.setValue(i/len(CITY_ID_NAME_MAP) * 100)

            scraped_projects = API.get_projects(city_id)

            if first_refresh:
                new_db[city_id] = scraped_projects
                continue

            old_projects = old_db.get(city_id, [])
            old_project_names = [p['name'] for p in old_projects]  # Assume names are unique
            for scraped_project in scraped_projects:
                if scraped_project['name'] not in old_project_names:
                    scraped_project['new'] = True

            new_db[city_id] = scraped_projects

        return new_db
