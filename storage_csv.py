import csv

class StorageCsv:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        data = {}
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    data[title] = {
                        'year': row['year'],
                        'rating': row['rating'],
                        'poster': row['poster']
                    }
        except FileNotFoundError:
            data = {}
        return data

    def write_data(self, data):
        try:
            with open(self.file_path, 'w', newline='') as file:
                fieldnames = ['title', 'year', 'rating', 'poster']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for title, details in data.items():
                    row = {'title': title, **details}
                    writer.writerow(row)
        except IOError:
            print(f"Error writing to file '{self.file_path}'")

    def list_movies(self):
        data = self.read_data()
        for movie in data.keys():
            print(movie)

    def delete_movie(self, title):
        data = self.read_data()
        if title in data:
            del data[title]
            self.write_data(data)
        else:
            print(f"Movie '{title}' not found")

    def add_movie(self, title, year, rating, poster):
        data = self.read_data()
        if title in data:
            print(f"Movie '{title}' already exists.")
        else:
            data[title] = {"year": year, "rating": rating, "poster": poster}
            self.write_data(data)

    def update_movie(self, title, rating):
        data = self.read_data()
        if title in data:
            data[title]["rating"] = rating
            self.write_data(data)
        else:
            print(f"Movie '{title}' not found")

if __name__ == "__main__":
    storage = StorageCsv('movies.csv')
    storage.add_movie('Inception', '2010', '8.8', "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg")
    storage.update_movie()



