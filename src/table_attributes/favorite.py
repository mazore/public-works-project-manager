from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt
from ..favorites_api import favorites_api


class Favorite(QCheckBox):
    def __init__(self, project):
        super().__init__()
        self.project = project
        if favorites_api.is_favorite(project):
            self.setCheckState(Qt.CheckState.Checked)  # Set checked

        self.stateChanged.connect(self.onStateChanged)

        style = 'padding-left: 12px;'
        if project.get('new'):
            style += 'background-color: yellow;'
        self.setStyleSheet(style)

    def onStateChanged(self, state):
        if state == 2:  # Checked
            favorites_api.add_favorite(self.project)
        elif state == 0:  # Unchecked
            favorites_api.remove_favorite(self.project)
