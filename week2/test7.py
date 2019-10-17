# -*- coding:utf-8 -*-


def function(array, left, right):
    if left < right:
        mid = int((left + right) / 2)
        function(array, left, mid)
        function(array, mid + 1, right)
        function1(array, left, mid, right)


def function1(array, left, mid, right):
    temp = [0] * len(array)
    i = left
    j = mid + 1
    t = 0
    while i <= mid and j <= right:
        if array[i] < array[j]:
            temp[t] = array[i]
            t += 1
            i += 1
        else:
            temp[t] = array[j]
            t += 1
            j += 1
    while i <= mid:
        temp[t] = array[i]
        t += 1
        i += 1
    while j <= right:
        temp[t] = array[j]
        t += 1
        j += 1
    t = 0
    while left <= right:
        array[left] = temp[t]
        left += 1
        t += 1


if __name__ == '__main__':
    array = [16, 9, 21, 13, 4, 11, 3, 22, 8, 7, 15, 29]
    function(array, 0, len(array) - 1)
    print(array)