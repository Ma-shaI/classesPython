# class Account:
#     __rate_usd = 0.013
#     __rate_eur = 0.011
#     __suffix = 'RUB'
#     __suffix_usd = 'USD'
#     __suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__surname = surname
#         self.__num = num
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.get_num()} принадлежащей {self.get_surname()} был открыт')
#         print("*" * 50)
#
#     def __del__(self):
#         print()
#         print('*' * 50)
#         print(f'Счет #{self.get_num()} принадлежащий {self.get_surname()} был закрыт.')
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
#     @staticmethod
#     def get_rate_usd():
#         return Account.__rate_usd
#
#     @staticmethod
#     def set_rate_usd(rate):
#         Account.__rate_usd = rate
#
#     @staticmethod
#     def set_rate_eur(rate):
#         Account.__rate_eur = rate
#
#     @staticmethod
#     def get_rate_eur():
#         return Account.__rate_eur
#
#     @staticmethod
#     def get_suffix():
#         return Account.__suffix
#
#     @staticmethod
#     def get_suffix_usd():
#         return Account.__suffix_usd
#
#     @staticmethod
#     def get_suffix_eur():
#         return Account.__suffix_eur
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.get_value()} {self.get_suffix()}')
#
#     def print_info(self):
#         print('Информация о счете')
#         print("-" * 20)
#         print(f'#{self.get_num()}')
#         print(f'Владелец: {self.get_surname()}')
#         self.print_balance()
#         print(f'Проценты: {self.get_percent():.0%}')
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.get_value(), Account.get_rate_usd())
#         print(f'Состояние счета: {usd_val} {self.get_suffix_usd()}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.get_value(), self.get_rate_eur())
#         print(f'Состояние счета: {eur_val} {self.get_suffix_eur()}')
#
#     def add_percent(self):
#         self.__value += self.get_value() * self.get_percent()
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, summa):
#         if summa > self.__value:
#             print(f'К сожалению у вас нет {summa} {self.get_suffix()}')
#             self.print_balance()
#         else:
#             self.__value -= summa
#             print(f'{summa} {self.get_suffix()} было успешно снято!')
#             self.print_balance()
#
#     def add_money(self, summa):
#         self.__value += summa
#         print(f'{summa} {self.get_suffix()} успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.set_rate_usd(2)
# acc.set_rate_eur(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_surname('Дюна')
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


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f'Счет #{self.num} принадлежащей {self.surname} был открыт')
        print("*" * 50)

    def __del__(self):

        print()
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        print('Информация о счете')
        print("-" * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print("-" * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, summa):
        if summa > self.value:
            print(f'К сожалению у вас нет {summa} {Account.suffix}')
            self.print_balance()
        else:
            self.value -= summa
            print(f'{summa} {Account.suffix} было успешно снято!')
            self.print_balance()

    def add_money(self, summa):
        self.value += summa
        print(f'{summa} {Account.suffix} успешно добавлено!')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.surname = 'Дюна'
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
