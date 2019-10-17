# -*- coding:utf-8 -*-


def function1(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex + 1
    while childIndex < length:
        if childIndex + 1 < length and array[childIndex + 1] > array[childIndex]:
            childIndex += 1
        if temp > array[childIndex]:
            break
        array[parentIndex] = array[childIndex];
        parentIndex = childIndex;
        childIndex = 2 * childIndex + 1;
    array[parentIndex] = temp


def function(array):
    for i in range(int((len(array) - 2) / 2), -1, -1):
        function1(array, i, len(array))
    for i in range(len(array) - 1, 0, -1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        function1(array, 0, i)


if __name__ == '__main__':
    array = [16, 9, 21, 13, 4, 11, 3, 22, 8, 7, 15, 29]
    function(array)
    print(array)
