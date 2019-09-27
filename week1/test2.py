# -*- coding:utf-8 -*-


def function1(a, b):
    x = a % b
    while x != 0:
        a = b
        b = x
        x = a % b
    return b


def function2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b
