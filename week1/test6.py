# -*- coding:utf-8 -*-


def function1(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n):
        a = a + b
        b = a - b
    return a


def function2(n):
    array = list()
    array[0] = 1
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    return array
