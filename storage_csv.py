import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        data = {}
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                # Print header
                print("CSV Headers:", reader.fieldnames)
                for row in reader:
                    # Print row to check if 'poster' exists
                    print("CSV Row:", row)
                    title = row.get('title')
                    if title:  # Check if title is not None
                        data[title] = {
                            'year': row.get('year', 'N/A'),
                            'rating': row.get('rating', 'N/A'),
                            'poster': row.get('poster', 'N/A')  # Default to 'N/A' if 'poster' is missing
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
        # Print each movie in a user-friendly format
        for title, details in data.items():
            print(f"Title: {title}, Year: {details['year']}, Rating: {details['rating']}, Poster: {details['poster']}")
        return data

    def delete_movie(self, title):
        data = self.read_data()
        if title in data:
            del data[title]
            self.write_data(data)
            print(f"Movie '{title}' deleted.")
        else:
            print(f"Movie '{title}' not found")

    def add_movie(self, title, year, rating, poster):
        data = self.read_data()
        if title in data:
            print(f"Movie '{title}' already exists.")
        else:
            data[title] = {"year": year, "rating": rating, "poster": poster}
            self.write_data(data)
            print(f"Movie '{title}' added.")

    def update_movie(self, title, rating):
        data = self.read_data()
        if title in data:
            data[title]["rating"] = rating
            self.write_data(data)
            print(f"Movie '{title}' updated.")
        else:
            print(f"Movie '{title}' not found")

if __name__ == "__main__":
    storage = StorageCsv('indian_movies.csv')
    # List current movies
    print("Current movies in CSV:")
    storage.list_movies()
    # Uncomment the following lines to test adding, deleting, and updating movies
    # Add a new movie
    # storage.add_movie('Abc', '2007', '5', 'image.png')

    # Delete a movie
    # storage.delete_movie('Abc')

    # Update a movie's rating
    # storage.update_movie('Inception', '9.0')

    # List movies again after modifications
    # print("\nUpdated movies in CSV:")
    # storage.list_movies()