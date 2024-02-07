# f(x) = x^2 - 2


def f1(x):
    result = x**2 - 2
    return result


f2 = lambda x: x**2 - 2


left, right = 0, 2


def bisect(f, left, right):

    value_left = f(left)
    value_right = f(right)

    if value_left * value_right > 0:
        raise ValueError("liczby są tych samych znaków")


def f1(x):
    result = x**2 - 2
    return result


f2 = lambda x: x**2 - 2


bisect(f2, 2, 4)
