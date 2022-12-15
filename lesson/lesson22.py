# продолжение ООП

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащей {self.surname} был открыт')
#         print("*" * 50)
#
#     def __del__(self):
#         print()
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете')
#         print("-" * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, summa):
#         if (summa > self.value):
#             print(f'К сожалению у вас нет {summa} {Account.suffix}')
#             self.print_balance()
#         else:
#             self.value -= summa
#             print(f'{summa} {Account.suffix} было успешно снято!')
#             self.print_balance()
#
#     def add_money(self, summa):
#         self.value += summa
#         print(f'{summa} {Account.suffix} успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюна')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)

import re

class UserData:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.__fio = fio
        self.__old = old
        self.__password = ps
        self.__weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.I))
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквы и дефис')

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or old < 14 or old > 120:  # or not 14< old<120
            raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError('Вес должен быть вещественным числом от 20кг')


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
