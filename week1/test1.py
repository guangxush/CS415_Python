# -*- coding:utf-8 -*-


def function1(array, low, high):
    if high > low:
        k = function2(array, low, high)
        function1(array, low, k - 1)
        function1(array, k + 1, high)


def function2(array, low, high):
    left = low
    right = high
    k = array[low]
    while left < right:
        while array[left] <= k:
            left += 1
        while array[right] > k:
            right = right - 1
        if left < right:
            array[left], array[right] = array[right], array[left]
    array[low] = array[right]
    array[right] = k
    return right
