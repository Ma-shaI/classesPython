import json


class Countries:

    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        self.file = 'countries.json'
        try:
            data = json.load(open(self.file, encoding='utf-8'))
        except FileNotFoundError:
            data = {}

        data[self.country] = self.capital

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add_data(self, country, capital):

        try:
            data = json.load(open(self.file, encoding='utf-8'))
        except FileNotFoundError:
            data = {}

        data[country] = capital

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print('Файл сохранен')

    def del_data(self, country):

        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data.get(country) is not None:
            del data[country]
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print('Файл сохранен')
        else:
            print('Такой страны нет. Проверьте написание или нажмите 5 для просмотра данных и повторите запрос')

    def get_data_by_country(self, country):

        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        item = data.get(country)
        if item is not None:
            print(f'Столица {country}: {item}')
        else:
            print('Такой страны в данном файле нет. Вы можете самостоятельно ввести данные')

    def get_data_by_capital(self, capital):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        key_cap = ''
        for k, v in data.items():
            if v == capital:
                key_cap = k

        if len(key_cap) > 0:
            print(f'Город {capital} является столицей {key_cap} ')
        else:
            print('Такой страны в данном файле нет. Вы можете самостоятельно ввести данные')

    def update_data(self, country, capital):

        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data.get(country) is not None:
            data[country] = capital
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print('Файл сохранен')
        else:
            print('Невозможно отредактировать данные, которых нет в файле')

    def read_data(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(data)


c1 = Countries('Россия', 'Москва')
text = f'{"*" * 40}\n' \
       f'Выбор действия:\n' \
       f'1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n' \
       f'5 - просмотр данных\n6 - завершение работы'

while True:
    print(text)
    try:
        n = int(input('Ввод: '))
        match n:
            case 1:
                name_country = input('Введите название страны (с заглавной буквы): ')
                name_capital = input("Введите название столицы страны (с заглавной буквы): ")
                c1.add_data(name_country, name_capital)
            case 2:
                name_country = input('Введите название страны (с заглавной буквы): ')
                c1.del_data(name_country)
            case 3:
                print('Выбор действия:\n1 - поиск по стране\n2-поиск по столице')
                m = int(input('Ввод: '))
                if m == 1:
                    name_country = input('Введите название страны (с заглавной буквы): ')
                    c1.get_data_by_country(name_country)
                elif m == 2:
                    name_capital = input("Введите название столицы страны (с заглавной буквы): ")
                    c1.get_data_by_capital(name_capital)
                else:
                    print('Другое число ты ввести не можешь')
            case 4:
                name_country = input('Введите название страны (с заглавной буквы): ')
                name_capital = input("Введите название столицы страны (с заглавной буквы): ")
                c1.update_data(name_country, name_capital)
            case 5:
                c1.read_data()
            case 6:
                print('Работа завершена')
                break
            case _:
                print('Внимательно прочитай, какие действия ты можешь выполнять')
                print('*'*40)
    except ValueError:
        print('Введите действие цифрой')

