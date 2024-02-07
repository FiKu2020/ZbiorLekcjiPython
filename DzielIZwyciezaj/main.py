# f(x) = x^2 - 2


def bisect(f, left, right):

    while True:
        value_left = f(left)
        value_right = f(right)

        if value_left * value_right > 0:
            raise ValueError("liczby są tych samych znaków")

        center = (left + right) / 2

        value_center = f(center)

        # print("\n\n")
        # print("left->", left, value_left)
        # print("right->", right, value_right)
        # print("center->", center, value_center)

        if value_left * value_center < 0:
            left = left
            right = center
        else:
            left = center
            right = right

        if right - left < 1e-14:
            return center


import math

a = 3
b = 4

f2 = lambda c: math.sqrt(a**2 + b**2) - c


result = bisect(f2, 3, 6)

print(result)
