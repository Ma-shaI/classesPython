# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian
# # from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())
from car import electrocar




def main():
    e_car = electrocar.ElectroCar('Tesla', 'T', '2020', 50000)
    e_car.show_car()
    e_car.description_battery()
    print('Stroka')
    print(__name__)


if __name__ == '__main__':
    main()
