class Power:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrap(a, b):
            return fn(a, b) ** self.n

        return wrap


@Power(4)
def func(a, b):
    return a * b


print(func(2, 2))
