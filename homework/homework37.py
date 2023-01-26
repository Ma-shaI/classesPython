import json


class Books:
    def __init__(self, title, author, publication_date, publisher, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.publisher = publisher
        self.price = price

    def __str__(self):
        return f'Название: {self.title}\nАвтор: {self.author}\nДата публикации: {self.publication_date}\nИздательство:'\
               f' {self.publisher}\nЦена: {self.price}'


b = Books('Мастер и Маргарита', 'Булгаков М.А.', 1967, 'АСТ', '300 рублей')

with open('books_data.json', 'w') as fw:
    json.dump(b, fw, indent=4, ensure_ascii=False, default=str)

with open('books_data.json', 'r') as fw:
    data = json.load(fw)
    print(data)
print('*'*50)
my_book = json.dumps(b, ensure_ascii=False, default=str)
data = json.loads(my_book)
print(data)
