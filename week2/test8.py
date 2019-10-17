# -*- coding:utf-8 -*-


def function():
    n = 0.0
    p = 1
    while p <= 100000:
        if p % 4 == 1:
            n = n + 1 / p
        else:
            n = n - 1 / p
        p = p + 2
    else:
        print(n * 4)


if __name__ == '__main__':
    function()
