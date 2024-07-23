import random
import matplotlib.pyplot as plt

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
        try:
            year = int(year)
            rating = float(rating)
            movies = self.storage.read_data()
            movies[title] = {'year': year, 'rating': rating}
            self.storage.write_data(movies)
            print(f"Movie '{title}' added successfully.")
        except ValueError:
            print("Invalid input. Year must be an integer and rating a float.")

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
        try:
            rating = float(rating)
            movies = self.storage.read_data()
            if title in movies:
                movies[title]['rating'] = rating
                self.storage.write_data(movies)
                print(f"Rating for movie '{title}' updated successfully.")
            else:
                print(f"Movie '{title}' not found.")
        except ValueError:
            print("Invalid input. Rating must be a float.")

    def random_movie(self):
        """Select and display a random movie from the database."""
        movies = self.storage.read_data()
        if movies:
            title, movie = random.choice(list(movies.items()))
            print(f"Random movie: {title} - Rating: {movie['rating']}, Year: {movie['year']}")
        else:
            print("No movies found.")

    def stats(self):
        """Display statistics of the movie collection."""
        movies = self.storage.read_data()
        if not movies:
            print("No movies in database.")
            return

        total_movies = len(movies)
        total_ratings = sum(movie['rating'] for movie in movies.values())
        average_rating = total_ratings / total_movies
        highest_rated = max(movies.items(), key=lambda x: x[1]['rating'])
        lowest_rated = min(movies.items(), key=lambda x: x[1]['rating'])

        print(f"Total movies: {total_movies}")
        print(f"Average rating: {average_rating:.2f}")
        print(f"Highest rated movie: {highest_rated[0]} with rating {highest_rated[1]['rating']}")
        print(f"Lowest rated movie: {lowest_rated[0]} with rating {lowest_rated[1]['rating']}")

    def _generate_website(self):
        """Generate a website (dummy method for this context)."""
        print("Website generation is not implemented yet.")

    def run(self):
        """Run the main loop of the application."""
        print("Movie app running...")

    def search_movie(self):
        """
        Search for a movie by name.
        """
        movies = self.storage.read_data()
        search_term = input("Enter the name of the movie to search: ")
        found = False
        for title, info in movies.items():
            if search_term.lower() in title.lower():
                print(f"{title}: Rating: {info['rating']}, Year: {info['year']}")
                found = True
        if not found:
            print("Movie not found.")

    def create_rating_histogram(self):
        """
        Create and save a histogram of movie ratings.
        """
        movies = self.storage.read_data()
        ratings = [info['rating'] for info in movies.values()]
        plt.hist(ratings, edgecolor='black')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        file_name = input("Enter filename to save the histogram (e.g., histogram.png): ")
        plt.savefig(file_name)
        print(f"Rating histogram saved to {file_name}")
