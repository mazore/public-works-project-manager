from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from datetime import datetime
from ..dt_helpers import format_datetime


class Time(QLabel):
    def __init__(self, project):
        text = format_datetime(project['dt'])
        if project['dt'] == datetime.min:
            text = project['time']
        super().__init__(text)

        self.setStyleSheet('margin-left: 5px')
