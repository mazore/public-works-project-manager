from PyQt6.QtWidgets import QLabel
from ..dt_helpers import format_time


class Time(QLabel):
    def __init__(self, project):
        text = format_time(project['dt'])
        super().__init__(text)

        self.setStyleSheet('margin-left: 2px')
