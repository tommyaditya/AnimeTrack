from models.anime import Anime
from models.datamanager import FileManager


class UserAnimeList:
    def __init__(self, data_file='data/anime_data.json'):
        self.file_manager = FileManager(data_file)
        self.anime_list = []
        self.load()

    def load(self):
        data = self.file_manager.load_data()
        self.anime_list = [Anime(**item) for item in data]

    def save(self):
        data = [anime.__dict__ for anime in self.anime_list]
        self.file_manager.save_data(data)

    def add_anime(self, anime):
        self.anime_list.append(anime)
        self.save()

    def remove_anime(self, title):
        self.anime_list = [a for a in self.anime_list if a.title.lower() != title.lower()]
        self.save()

    def update_anime(self, title, **kwargs):
        for anime in self.anime_list:
            if anime.title.lower() == title.lower():
                for key, value in kwargs.items():
                    if hasattr(anime, key):
                        setattr(anime, key, value)
                self.save()
                return True
        return False

    def list_anime(self):
        return self.anime_list

    def find_anime(self, title):
        for anime in self.anime_list:
            if anime.title.lower() == title.lower():
                return anime
        return None