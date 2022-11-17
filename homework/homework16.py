def get_average(fn):
    def wrap(*args):
        s = [str(i) for i in args]
        return 'Среднее арифметическое чисел', ', '.join(s), '=', fn(*args) / len(args)

    return wrap


@get_average
def get_sum(*args):
    s = [str(i) for i in args]
    print('Сумма чисел', ', '.join(s), '=', sum(args))
    return sum(args)


print(*get_sum(2, 3, 3, 4))