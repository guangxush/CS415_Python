### 题目1：描述function1的功能

```python
def function1(x):
    for i in range(2, x):
        while x != 1:
            if x % i == 0:
                print(i, '*', end='')
                x /= i
            else:
                break
    print('\b ', end='')

```

### 题目2：描述function1和function2的功能

```python
def function1(x):
    for i in range(-x, x + 1):
        if i < 0:
            j = -i
        else:
            j = i
        print(' ' * j + '*' * (2 * x + 1 - 2 * j))


def function2(x):
    for i in range(-x, x + 1):
        if i < 0:
            j = -i
        else:
            j = i
        print(' ' * ((2 * x + 1) // 2 - j) + '*' * (2 * j + 1))
```


### 题目3：描述function的功能

```python
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
```


### 题目4：描述function的功能

```python
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
```


### 题目5：描述function的功能

```python
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
```


### 题目6：描述function的功能

```python
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

```


### 题目7：描述function的功能

```python
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
```


### 题目8：描述function的功能

```python
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
```
