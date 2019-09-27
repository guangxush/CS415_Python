# -*- coding:utf-8 -*-


"""
a说我不是小偷；
b说c是小偷；
c说小偷是d；
d说c胡说！
"""


def function():
    for thief in ('a', 'b', 'c', 'd'):
        sum = ('a' != thief) + (thief == 'c') + (thief == 'd') + (thief != 'd')
        if sum == 3:
            print("thief is %s" % thief)


def function1(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(length):
        matrix[i] = matrix[i][::-1]
