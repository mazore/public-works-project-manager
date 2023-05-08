from PyQt6.QtWidgets import QWidget, QPushButton, QProgressBar, QHBoxLayout
from PyQt6.QtCore import Qt, QObject, QThread, pyqtSignal
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
        self.progress_bar.setMaximum(len(CITY_ID_NAME_MAP))
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.progress_bar)

        # layout.addStretch()

    def refresh(self):
        if os.path.exists('db.json'):
            with open('db.json') as f:
                old_db = json.load(f)
        else:
            old_db = {}

        self.worker = RefreshWorker(old_db)
        self.refreshThread = QThread()
        self.worker.moveToThread(self.refreshThread)
        self.refreshThread.started.connect(self.worker.run)
        self.worker.progress.connect(self.reportProgress)

        self.worker.finished.connect(self.refreshFinished)
        self.worker.finished.connect(self.worker.deleteLater)
        self.refreshThread.finished.connect(self.refreshThread.deleteLater)

        self.refreshThread.start()

    def refreshFinished(self):
        self.progress_bar.setFormat('')
        self.progress_bar.setValue(0)

        self.window.load_data_from_db_file()
        self.window.table.setup()

        self.refreshThread.quit()

    def reportProgress(self, i, city_name):
        print(f'{i}/{len(CITY_ID_NAME_MAP)}: {city_name}')
        self.progress_bar.setValue(i)
        self.progress_bar.setFormat('%p%: Loading ' + city_name)


class RefreshWorker(QObject):
    """Uses a new thread to run the longer process of scraping all sites and storing them to the db"""
    finished = pyqtSignal()
    progress = pyqtSignal(int, str)

    def __init__(self, old_db):
        super().__init__()
        self.old_db = old_db
        self.first_refresh = not old_db

    def run(self):
        new_db = {}

        i = 0
        for city_id, name in CITY_ID_NAME_MAP.items():
            i += 1
            self.progress.emit(i, name)

            scraped_projects = API.get_projects(city_id)

            if self.first_refresh:
                new_db[city_id] = scraped_projects
                continue

            old_projects = self.old_db.get(city_id, [])
            old_project_names = [p['name'] for p in old_projects]  # Assume names are unique
            for scraped_project in scraped_projects:
                if scraped_project['name'] not in old_project_names:
                    scraped_project['new'] = True

            new_db[city_id] = scraped_projects

        with open('db.json', 'w') as f:
            json.dump(new_db, f, indent=4)

        self.finished.emit()
