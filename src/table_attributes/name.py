from PyQt6.QtWidgets import QLabel


class Name(QLabel):
    def __init__(self, project):
        super().__init__(project['name'])
        self.setStyleSheet('margin-left: 5px')
