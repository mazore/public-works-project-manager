from msilib import Table
from .base import TableAttrBase
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
import webbrowser


class Url(TableAttrBase):
    def __init__(self, project):
        style = '''
            color: blue;
            text-decoration: underline;
            padding: 0 10px 0 10px;
        '''
        super().__init__(project, 'link', style)
        self.url = project['url']

        cursor = QCursor()
        cursor.setShape(Qt.CursorShape.PointingHandCursor)
        self.setCursor(cursor)

    def mousePressEvent(self, _):
        webbrowser.open(self.url)
