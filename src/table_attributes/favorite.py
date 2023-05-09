from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt
import os.path
import json

print('loading favorites data')
if not os.path.exists('favorites.json'):
    print('creating new favorites file')
    with open('favorites.json', 'w') as f:
        json.dump([], f)
    favorites = []
else:
    with open('favorites.json') as f:
        favorites = json.load(f)

# Remove duplicates just in case
favorites = list(set(favorites))


class Favorite(QCheckBox):
    def __init__(self, project):
        super().__init__()
        self.project = project
        if project['url'] in favorites:
            self.setCheckState(Qt.CheckState.Checked)  # Set checked

        self.stateChanged.connect(self.onStateChanged)

        style = 'padding-left: 12px;'
        if project.get('new'):
            style += 'background-color: yellow;'
        self.setStyleSheet(style)

    def onStateChanged(self, state):
        if state == 2:  # Checked
            favorites.append(self.project['url'])
        elif state == 0:  # Unchecked
            favorites.remove(self.project['url'])

        with open('favorites.json', 'w') as f:
            json.dump(favorites, f, indent=4)
