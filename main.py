from colorama import Fore, init
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    init(autoreset=True)

    print(Fore.CYAN + "Choose storage format:")
    print(Fore.CYAN + "1. JSON")
    print(Fore.CYAN + "2. CSV")
    storage_choice = input(Fore.YELLOW + "Enter choice (1-2): ")

    if storage_choice == '1':
        storage_instance = StorageJson('Indian_movies.json')
    elif storage_choice == '2':
        storage_instance = StorageCsv('movies.csv')
    else:
        print(Fore.RED + "Invalid choice. Defaulting to JSON.")
        storage_instance = StorageJson('Indian_movies.json')

    app = MovieApp(storage_instance)

    while True:
        print(Fore.CYAN + "********** My Movies Database **********")
        print(Fore.CYAN + "Menu:")
        print(Fore.CYAN + "1. List movies")
        print(Fore.CYAN + "2. Add movie")
        print(Fore.CYAN + "3. Delete movie")
        print(Fore.CYAN + "4. Update movie")
        print(Fore.CYAN + "5. Exit")

        choice = input(Fore.YELLOW + "Enter choice (1-5): ")

        if choice == '1':
            app.list_movies()
        elif choice == '2':
            title = input("Enter movie title: ")
            year = int(input("Enter release year: "))
            rating = float(input("Enter rating: "))
            app.add_movie(title, year, rating)
        elif choice == '3':
            title = input("Enter movie title to delete: ")
            app.delete_movie(title)
        elif choice == '4':
            title = input("Enter movie title to update: ")
            rating = float(input("Enter new rating: "))
            app.update_movie(title, rating)
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
