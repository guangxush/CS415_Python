# -*- coding:utf-8 -*-


def function(x):
    for i in range(-x, x + 1):
        if i < 0:
            j = -i
        else:
            j = i
        print(' ' * j + '*' * (2 * x + 1 - 2 * j))


def function(x):
    for i in range(-x, x + 1):
        if i < 0:
            j = -i
        else:
            j = i
        print(' ' * ((2 * x + 1) // 2 - j) + '*' * (2 * j + 1))
