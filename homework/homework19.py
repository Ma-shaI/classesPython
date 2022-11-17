import re


def replace_word(txt, word='о'):
    count = txt.count(word)
    text = test.replace(word.lower(), word.upper(), count - 1)
    text = text.replace(word.upper(), word.lower(), 1)
    return text


s = input('Введите строку: ')
w = input('Введите букву: ')
test = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'
if len(w) == 1:
    print(replace_word(s, w))
else:
    print("Я изменю букву по умолчанию")
    print(replace_word(s))
print(test)

