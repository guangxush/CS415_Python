# -*- coding:utf-8 -*-
import math


def function(fun, start, end, precision):
    s = fun(start)
    e = fun(end)
    if e * s > 0:
        return False
    if s == 0:
        return start
    if e == 0:
        return end
    while abs(end - start) > precision:
        mid = (start + end) / 2.0
        m = fun(mid)
        if m == 0:
            return mid
        if s * m < 0:
            end = mid
        if m * e < 0:
            start = mid
    return start


def func(x):
    return 2 * math.pow(x, 2) + 5 * x - 20
