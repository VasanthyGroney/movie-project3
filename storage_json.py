from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def write_data(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError:
            print(f"Error writing to file '{self.file_path}'")

    def list_movies(self):
        data = self.read_data()
        for movie in data.keys():
            print (movie)

    def delete_movie(self, title):
        data = self.read_data()
        data.pop(title)
        self.write_data(data)


    def add_movie(self, title, year, rating, poster):
        data = self.read_data()
        data [title] = {"year": year, "rating": rating, "poster": poster}
        self.write_data(data)

    def update_movie(self, title, rating):
        data = self.read_data()
        data[title]["rating"] = rating
        self.write_data(data)

if __name__ == "__main__":
    storage = StorageJson('indian_movies.json')
    #print(storage.list_movies())
    #storage.add_movie('Abc',2007, 5, 'image.png')
    #storage.delete_movie('Abc')


