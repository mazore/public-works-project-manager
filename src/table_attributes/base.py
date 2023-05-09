from PyQt6.QtWidgets import QLabel


class TableAttrBase(QLabel):
    def __init__(self, project, text, style):
        super().__init__(text)

        if project.get('new'):
            style += 'background-color: yellow;'

        self.setStyleSheet(style)
