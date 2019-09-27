# -*- coding:utf-8 -*-


def function(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = round((low + high) / 2)
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
