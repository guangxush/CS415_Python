# -*- coding:utf-8 -*-
from math import sqrt


def function1(num):
    x = sqrt(num)
    y = num / 2.0
    low = 0.0
    up = num * 1.0
    count = 1
    while abs(y - x) > 0.00000001:
        count += 1
        if y * y > num:
            up = y
            y = low + (y - low) / 2
        else:
            low = y
            y = up - (up - y) / 2
    return y


def function2(num):
    x = sqrt(num)
    y = num / 2.0
    count = 1
    while abs(y - x) > 0.00000001:
        count += 1
        y = ((y * 1.0) + (1.0 * num) / y) / 2.0000
    return y
