# < Іваньо Іван >
# Лабораторна робота № 5.2
# Обчислення суми ряду Тейлора за допомогою функцій.
# Варіант 0.6

import math

# X_start = -1
# X_end = 0.9
# dX = 0.1
# eps = 0.000001


X_start = float(input("X_поч: "))
X_end = float(input("X_кін: "))
dX = float(input("dX: "))
eps = float(input("eps: "))

n = 1
n1 = 0
s = 0

print('----------------------------------------')
print('|   X   |   ln(1 - x)  |   S   |   n   |')
print('----------------------------------------')


def A(x, n, a):
    r = x * (n - 1) / n
    a *= r
    return a


def S(x, eps):
    n = 1
    a = x
    s = a
    while abs(a) > eps:
        n += 1
        a = A(x, n, a)
        s += a
    global n1
    n1 = n
    return s


x = X_start

while x <= X_end:

    print('|   {0}   |   {1}   |   {2}   |   {3}   |'.format(str(round(x, 4)), str(round(math.log(1 - x), 4)),
                                                             str(round(-S(x, eps), 4)), str(n1)))
    x += dX

print('----------------------------------------')
