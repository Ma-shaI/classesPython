import json


class Books:
    def __init__(self, title, author, publication_date, publisher, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.publisher = publisher
        self.price = price
        self.c = lambda x: x*x

    # def __str__(self):
    #     return f'Название: {self.title}\nАвтор: {self.author}\nДата публикации: {self.publication_date}\nИздательство
    #     :' \
    #            f' {self.publisher}\nЦена: {self.price}'

    def info(self):
        return f'Название: {self.title}\nАвтор: {self.author}\nДата публикации: {self.publication_date}\nИздательство:' \
               f' {self.publisher}\nЦена: {self.price}\nLambda: {self.c(6)}'


b = Books('Мастер и Маргарита', 'Булгаков М.А.', 1967, 'АСТ', '300 рублей')
c = b.info()
# with open('books_data.json', 'w') as fw:
#     json.dump(b, fw, indent=4, ensure_ascii=False, default=str)
#
# with open('books_data.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)
print('*' * 50)
my_book = json.dumps(c, ensure_ascii=False)
data = json.loads(my_book)
print(data)
