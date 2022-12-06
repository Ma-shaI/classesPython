class Book:
    title = 'title'
    year = '0000'
    publisher = 'publisher'
    genre = 'genre'
    author = 'author'
    price = 'price'

    def input_book(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def print_book(self):
        print(' Данные о книге '.center(40, '*'))
        print(f'Название книги: {self.title}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\n'
              f'Жанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}')
        print('='*40)

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year =year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher=publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre=genre

    def get_genre(self):
        return  self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.print_book()
b1.input_book('Безмолвный пациент', '2019', "Эксмо", "Триллер", "Алекс Михаэлидес", "319 рублей")
b1.print_book()
b1.set_title("Цветы для Элджернона")
print(b1.get_title())
b1.set_year('2016')
print(b1.get_year())
b1.set_publisher('Эксмо-М')
print(b1.get_publisher())
b1.set_genre('Фантастика')
print(b1.get_genre())
b1.set_author('Дэниел Киз')
print(b1.get_author())
b1.set_price('219 рублей')
print(b1.get_price())
b1.print_book()