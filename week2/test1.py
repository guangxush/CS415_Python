# -*- coding:utf-8 -*-


def function1(x):
    for i in range(2, x):
        while x != 1:
            if x % i == 0:
                print(i, '*', end='')
                x /= i
            else:
                break
    print('\b ', end='')
