# -*- coding:utf-8 -*-


def function(matrix):
    result = []
    i, p = 0, 0
    m, n = len(matrix[0]), len(matrix)
    while p != m * n:
        l, h = n - i - 1, m - i - 1
        for y in range(i, m - i):
            result.append(matrix[y][i])
            p += 1
        for x in range(i + 1, n - i):
            result.append(matrix[h][x])
            p += 1
        for y in range(h - 1, i - 1, -1):
            result.append(matrix[y][l])
            p += 1
        for x in range(l - 1, i, -1):
            result.append(matrix[i][x])
            p += 1
        i += 1
    return result
