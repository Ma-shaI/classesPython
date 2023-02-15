from model import MoviesModal
from view import UserInterface


class Controller:
    def __init__(self):
        self.movies_model = MoviesModal()
        self.user_interface = UserInterface()

    def run(self):
        choice = None
        while choice != 'q':
            choice = self.user_interface.editing_catalog_movies()
            self.check_user_choice(choice)

    def check_user_choice(self, choice):
        if choice == '1':
            movies = self.user_interface.add_user_movie()
            self.movies_model.add_movies(movies)
        elif choice == '2':
            movies = self.movies_model.get_catalog_movies()
            self.user_interface.show_catalog_movies(movies)
        elif choice == '3':
            movie_title = self.user_interface.get_user_movie()
            try:
                movie = self.movies_model.get_single_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_key(movie_title)
            else:
                self.user_interface.show_single_movie(movie)
        elif choice == '4':
            movie_title = self.user_interface.get_user_movie()
            try:
                title = self.movies_model.del_single_movie(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_key(movie_title)
            else:
                self.user_interface.show_del_movie(title)

        elif choice == 'q':
            self.movies_model.save_data()
        else:
            self.user_interface.show_incorrect_choice(choice)
