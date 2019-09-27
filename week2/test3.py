# -*- coding:utf-8 -*-


def function(year, month, day):
    count = day
    for i in range(1, month):
        count += function1(year, month)
    return count


def function1(year, month):
    day = 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = 31
    elif month in (4, 6, 9, 11):
        day = 30
    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = 29
        else:
            day = 28
    return day
