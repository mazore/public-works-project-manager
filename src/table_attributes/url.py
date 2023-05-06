from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
import webbrowser


class Url(QLabel):
    def __init__(self, project):
        super().__init__('link')
        self.setStyleSheet('''
            color: blue;
            text-decoration: underline;
            margin: 0 20px 0 20px;
        ''')
        self.url = project['url']

        cursor = QCursor()
        cursor.setShape(Qt.CursorShape.PointingHandCursor)
        self.setCursor(cursor)

    def mousePressEvent(self, _):
        webbrowser.open(self.url)
