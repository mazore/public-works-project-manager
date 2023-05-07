from PyQt6.QtWidgets import QLabel
from ..city_data import CITY_ID_NAME_MAP


class City(QLabel):
    def __init__(self, project):
        super().__init__(CITY_ID_NAME_MAP.get(project['city_id'], 'Error: Unknown City'))

        self.setStyleSheet('margin-left: 5px;')
