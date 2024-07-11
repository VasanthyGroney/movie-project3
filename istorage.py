from abc import ABC, abstractmethod


class IStorage(ABC):
    """
        IStorage is an abstract base class - defines interface for a movie storage system.
        Classes from IStorage must implement the abstract methods:
        - list_movies
        - add_movie
        - delete_movie
        - update_movie
        """

    @abstractmethod
    def list_movies(self):
        """ Displays the title of movies in the data base """
        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
                Add a new movie to the storage. Returns-None """
        pass


    @abstractmethod
    def delete_movie(self, title):
        """
                        Delete a new movie to the storage. Returns-None """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """ Update the rating of a movie in the storage.Returns-None """
        pass
