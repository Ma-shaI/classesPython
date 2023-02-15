def add_title(title):
    def middle(fn):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, "="))
            func = fn(*args, **kwargs)
            print('=' * 50)
            return func

        return wrap

    return middle


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def editing_catalog_movies(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4- удаление фильма'
              '\nq - выход из программы')
        choice = input('Выберите вариант действия: ')
        return choice

    @add_title('Добавление фильма')
    def add_user_movie(self):
        dict_movies = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None
        }
        for key in dict_movies:
            dict_movies[key] = input(f'Введите {key} фильма: ')
        return dict_movies

    @add_title('Каталог фильмов')
    def show_catalog_movies(self, catalog_movies):
        for ind, key in enumerate(catalog_movies, 1):
            print(f'{ind}) {key}')

    @add_title('Ввод название фильма')
    def get_user_movie(self):
        movie = input('Введите название фильма: ')
        return movie

    @add_title('Просмотр фильма')
    def show_single_movie(self, dict_movie):
        for key in dict_movie:
            print(f'{key} фильма: {dict_movie[key]}')

    @add_title('Ошибка')
    def show_incorrect_key(self, key):
        print(f'Фильма с названием {key} нет в нашем каталоге')

    @add_title('Удаление фильма')
    def show_del_movie(self, title):
        print(f'Фильм с названием {title} удален')

    @add_title('Ошибка')
    def show_incorrect_choice(self, choice):
        print(f'Действия {choice} нет. Выберите другое действие')