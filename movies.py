import json
from random import choice
from matplotlib import pyplot as plt


FILE_PATH = 'indian_movies.json'

def get_movies():
    """
    Retrieve all movies from the JSON file.

    Returns:
        dict: A dictionary containing movies data.
    """
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"movies": []}
    except json.JSONDecodeError:
        return {"movies": []}

def save_movies(data):
    """
    Save movies data to the JSON file.
    """
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def add_movie(title, year, rating):
    """
    Add a new movie to the JSON file.

    """
    data = get_movies()
    movies = data["movies"]

    if not any(movie["title"].lower() == title.lower() for movie in movies):
        new_movie = {
            "id": max(movie["id"] for movie in movies) + 1 if movies else 1,
            "title": title,
            "genre": [],
            "director": "",
            "cast": [],
            "release_date": year,
            "duration": 0,
            "ratings": {
                "IMDb": rating,
                "Rotten Tomatoes": 0,
                "Metacritic": 0
            },
            "synopsis": ""
        }
        movies.append(new_movie)
        save_movies(data)
        print(f'Movie "{title}" with rating {rating} is successfully added.')
    else:
        print(f'Movie "{title}" already exists.')

def delete_movie(title):
    """
    Delete a movie from the JSON file.

    Args:
        title (str): The title of the movie to delete.
    """
    data = get_movies()
    movies = data["movies"]
    movies = [movie for movie in movies if movie["title"].lower() != title.lower()]
    data["movies"] = movies
    save_movies(data)
    print(f'Movie "{title}" is successfully deleted.')

def update_movie(title, rating):
    """
    Update the rating of an existing movie in the JSON file.
    """
    data = get_movies()
    movies = data["movies"]
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["ratings"]["IMDb"] = rating
            save_movies(data)
            print(f'Rating for movie "{title}" updated successfully.')
            return
    print(f'Movie "{title}" not found.')


def list_movies():
    """
    List all movies in the JSON file.
    """
    data = get_movies()
    movies = data["movies"]
    if not movies:
        print("No movies in the list")
    else:
        for movie in movies:
            print(f"Title: {movie['title']}")


def movie_stats():
    """
    Display statistics about the movies.
    """
    data = get_movies()
    movies = data["movies"]
    if not movies:
        print("No movies found.")
        return

    total_movies = len(movies)
    ratings = sorted(movie['ratings']['IMDb'] for movie in movies)
    average_rating = sum(ratings) / total_movies
    median_index = total_movies // 2
    median_rating = (ratings[median_index] + ratings[~median_index]) / 2
    best_rating, worst_rating = max(ratings), min(ratings)
    best_movies = [movie['title'] for movie in movies if movie['ratings']['IMDb'] == best_rating]
    worst_movies = [movie['title'] for movie in movies if movie['ratings']['IMDb'] == worst_rating]

    print("\n*** Movie Stats ***")
    print(f"Total movies: {total_movies}")
    print(f"Average rating: {average_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")
    print("Best movie(s) by rating:")
    for movie in best_movies:
        print(f"{movie} - Rating: {best_rating}")
    print("\nWorst movie(s) by rating:")
    for movie in worst_movies:
        print(f"{movie} - Rating: {worst_rating}")


def random_movie():
    """
    Select and display a random movie from the database.
    """
    data = get_movies()
    movies = data["movies"]
    if movies:
        movie = choice(movies)
        print(f"Random movie: {movie['title']} - Rating: {movie['ratings']['IMDb']}, Year: {movie['release_date']}")
    else:
        print("No movies found.")


def search_movie():
    """
    Search for a movie by name.
    """
    data = get_movies()
    movies = data["movies"]
    search_term = input("Enter the name of the movie to search: ")
    found = False
    for movie in movies:
        if search_term.lower() in movie["title"].lower():
            print(f"{movie['title']}: Rating: {movie['ratings']['IMDb']}, Year: {movie['release_date']}")
            found = True
    if not found:
        print("Movie not found.")


def movies_sorted_by_rating():
    """
    List movies sorted by rating.
    """
    data = get_movies()
    movies = data["movies"]
    if movies:
        sorted_movies = sorted(movies, key=lambda x: x['ratings']['IMDb'], reverse=True)
        print("\n*** Movies Sorted by Rating ***")
        for movie in sorted_movies:
            print(f"{movie['title']}: Rating: {movie['ratings']['IMDb']}, Year: {movie['release_date']}")
    else:
        print("No movies found in the database.")


def create_rating_histogram():
    """
    Create and save a histogram of movie ratings.
    """
    data = get_movies()
    movies = data["movies"]
    ratings = [movie['ratings']['IMDb'] for movie in movies]
    plt.hist(ratings, edgecolor='black')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    file_name = input("Enter filename to save the histogram (e.g., histogram.png): ")
    plt.savefig(file_name)
    print(f"Rating histogram saved to {file_name}")






