from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from ..dt_helpers import format_datetime


class Time(QLabel):
    def __init__(self, dt):
        super().__init__(format_datetime(dt))
