from datetime import date


class Cars:
    def __init__(self, model, year, producer, engine, color, price):
        self.model = model
        self.year = year
        self.producer = producer
        self.engine = engine
        self.color = color
        self.price = price

    @staticmethod
    def verify_model(model):
        if not isinstance(model, str):
            raise TypeError('Название модели должно быть строкой')

    @staticmethod
    def verify_year(year):
        if not isinstance(year, int):
            raise TypeError('Год выпуска должен быть цифрой')
        current_date = date.today()
        if year > current_date.year:
            raise TypeError(f'Год выпуска не может быть больше чем {current_date.year}')

    @staticmethod
    def verify_producer(producer):
        if not isinstance(producer, str):
            raise TypeError("Производитель должен быть строкой")

    @staticmethod
    def verify_engine(engine):
        if not isinstance(engine, str):
            raise TypeError('Мощность двигателя должна быть строкой')

    @staticmethod
    def verify_color(color):
        if not isinstance(color, str):
            raise TypeError('Цвет машины должен быть строкой')

    @staticmethod
    def verify_price(price):
        if not isinstance(price, int):
            raise TypeError('Цена должна быть цифрой')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.verify_model(model)
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, producer):
        self.verify_producer(producer)
        self.__producer = producer

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.verify_engine(engine)
        self.__engine = engine

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.verify_color(color)
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.verify_price(price)
        self.__price = price

    def info_car(self):
        print('*' * 10, "Данные автомобиля", '*' * 10)
        print('Название модели:', self.__model)
        print('Год выпуска:', self.__year)
        print('Производитель:', self.__producer)
        print('Мощность двигателя:', self.__engine)
        print('Цвет машины:', self.__color)
        print('Цена:', self.__price)
        print('=' * 40)


car1 = Cars('X7 M50i', 2021, 'BMW', '530 л.с.', 'white', 10790000)
car1.info_car()

