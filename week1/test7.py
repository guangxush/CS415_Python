# -*- coding:utf-8 -*-


def function1(nums, target):
    d = {}
    n = len(nums)
    for x in range(n):
        a = target - nums[x]
        if nums[x] in d:
            return d[nums[x]], x
        else:
            d[a] = x


def function2(nums, target):
    l = len(nums)
    for i in range(l):
        another = target - nums[i]
        if another in nums:
            j = nums.index(another)
            if i == j:
                continue
            else:
                return [i, j]


def function3(nums, target):
    l = len(nums)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if nums[i] + nums[j] == target:
                return [i, j]
