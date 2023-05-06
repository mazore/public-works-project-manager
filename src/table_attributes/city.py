from PyQt6.QtWidgets import QLabel


# TODO: This is really bad to have here, we should only be loading this data once not for every table row
# !!!!!!!!!!!!!!!!!!!!!!!!!
CITY_ID_NAME_MAP = {}
is_header = True
for line in open('city_ids.csv'):
    if is_header:
        is_header = False
        continue
    id, name = line.strip('\n').split(',', 1)
    CITY_ID_NAME_MAP[id] = name


class City(QLabel):
    def __init__(self, project):
        super().__init__(CITY_ID_NAME_MAP[project['city_id']])

        self.setStyleSheet('margin-left: 5px;')
