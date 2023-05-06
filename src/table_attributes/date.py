from PyQt6.QtWidgets import QLabel
from datetime import datetime
from ..dt_helpers import format_date


class Date(QLabel):
    def __init__(self, project):
        text = format_date(project['dt'])
        if project['dt'] == datetime.min:
            text = project['time']
        super().__init__(text)

        self.setStyleSheet('margin-left: 5px')
