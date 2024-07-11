class MovieApp:
    def __init__(self, storage_instance):
        """Initialize with a storage instance."""
        self.storage = storage_instance

    def list_movies(self):
        """List all movies in the storage."""
        movies = self.storage.read_data()
        if movies:
            print("Movies in database:")
            for title, info in movies.items():
                print(f"Title: {title}, Year: {info['year']}, Rating: {info['rating']}")
        else:
            print("No movies in database.")

    def add_movie(self, title, year, rating):
        """Add a new movie to the storage."""
        movies = self.storage.read_data()
        movies[title] = {'year': year, 'rating': rating}
        self.storage.write_data(movies)
        print(f"Movie '{title}' added successfully.")

    def delete_movie(self, title):
        """Delete a movie from the storage."""
        movies = self.storage.read_data()
        if title in movies:
            del movies[title]
            self.storage.write_data(movies)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, rating):
        """Update the rating of an existing movie."""
        movies = self.storage.read_data()
        if title in movies:
            movies[title]['rating'] = rating
            self.storage.write_data(movies)
            print(f"Rating for movie '{title}' updated successfully.")
        else:
            print(f"Movie '{title}' not found.")
