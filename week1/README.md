### 题目1：描述function1的功能

```python
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

```

### 题目2：描述function1和function2的功能

```python
def function1(a, b):
    x = a % b
    while x != 0:
        a = b
        b = x
        x = a % b
    return b


def function2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b
```


### 题目3：描述function的功能

```python
def function(array):
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            array.append(i)
    return array
```


### 题目4：描述function的功能

```python
def function(fun, start, end, precision):
    s = fun(start)
    e = fun(end)
    if e * s > 0:
        return False
    if s == 0:
        return start
    if e == 0:
        return end
    while abs(end - start) > precision:
        mid = (start + end) / 2.0
        m = fun(mid)
        if m == 0:
            return mid
        if s * m < 0:
            end = mid
        if m * e < 0:
            start = mid
    return start


def func(x):
    return 2 * math.pow(x, 2) + 5 * x - 20
```


### 题目5：描述function1 2的功能

```python
def function1(num):
    x = sqrt(num)
    y = num / 2.0
    low = 0.0
    up = num * 1.0
    count = 1
    while abs(y - x) > 0.00000001:
        count += 1
        if y * y > num:
            up = y
            y = low + (y - low) / 2
        else:
            low = y
            y = up - (up - y) / 2
    return y


def function2(num):
    x = sqrt(num)
    y = num / 2.0
    count = 1
    while abs(y - x) > 0.00000001:
        count += 1
        y = ((y * 1.0) + (1.0 * num) / y) / 2.0000
    return y
```


### 题目6：描述function1 2的功能

```python
def function1(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n):
        a = a + b
        b = a - b
    return a


def function2(n):
    array = list()
    array[0] = 1
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    return array

```


### 题目7：描述function1 2 3的功能

```python
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

```


### 题目8：描述function1 2的功能

```python
def function1():
    for thief in ('a', 'b', 'c', 'd'):
        sum = ('a' != thief) + (thief == 'c') + (thief == 'd') + (thief != 'd')
        if sum == 3:
            print("thief is %s" % thief)


def function2(matrix):
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(length):
        matrix[i] = matrix[i][::-1]

```
