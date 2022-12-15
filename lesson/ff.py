import re
class UserData:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.__fio = fio
        self.__old = old
        self.__password = ps
        self.__weight = weight



    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Игорь', 'Глебович']
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE)  # ВолковИгорьНиколаевич
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")


p1 = UserData("Волков Игорь Глебович", 25, "1234 567890", 80.8)
s = " Hello  "


