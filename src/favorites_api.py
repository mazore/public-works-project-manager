import os.path
import json


class FavoritesAPI:
    def __init__(self):
        print('loading favorites data')
        if not os.path.exists('favorites.json'):
            print('creating new favorites file')
            with open('favorites.json', 'w') as f:
                json.dump([], f)
            self.favorites = []
        else:
            with open('favorites.json') as f:
                self.favorites = json.load(f)

        # Remove duplicates just in case
        self.favorites = list(set(self.favorites))

    def is_favorite(self, project):
        return project['url'] in self.favorites

    def save_to_file(self):
        with open('favorites.json', 'w') as f:
            json.dump(self.favorites, f, indent=4)

    def add_favorite(self, project):
        self.favorites.append(project['url'])
        self.save_to_file()

    def remove_favorite(self, project):
        self.favorites.remove(project['url'])
        self.save_to_file()


favorites_api = FavoritesAPI()
