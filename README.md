# MovieApp

MovieApp is a simple command-line application for managing a movie database. Users can add, list, update, delete, and search movies, as well as generate statistics and select a random movie. The application supports storage in both JSON and CSV formats.

## Features

- **List Movies**: Display all movies in the database.
- **Add Movie**: Add a new movie with its title, release year, and rating.
- **Delete Movie**: Remove a movie from the database.
- **Update Movie**: Update the rating of an existing movie.
- **Random Movie**: Select and display a random movie from the database.
- **Stats**: Display statistics of the movie collection including total movies, average rating, highest rated movie, and lowest rated movie.
- **Search Movie**: Search for a movie by name.
- **Generate Website**: Dummy method for generating a website (not implemented yet).
- **Run**: Start the movie app (dummy method for this context).
- **Create Rating Histogram**: Generate and save a histogram of movie ratings.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MovieApp.git
    cd MovieApp
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the following Python files in the project directory:
    - `movie_app.py`
    - `storage_json.py`
    - `storage_csv.py`

## Usage

Run the application:
```bash
python main.py
