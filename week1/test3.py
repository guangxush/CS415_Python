# -*- coding:utf-8 -*-


def function(array):
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            array.append(i)
    return array
