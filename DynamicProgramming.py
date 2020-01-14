"""
Basic Dynamic programming with fibonacci numbers.
It's using memoization methodology
It's not to repeat the same process. ex) when using recursion for fibonacci number
"""


def fibo(num):

    if num < 2:#when the value's smaller than 2
        return num
    else:
        cache = [0 for _ in range(num + 1)]#declare a cache for memoization

        cache[0] = 0
        cache[1] = 1

        for idx in range(2, num + 1):#cache value from '2'
            cache[idx] = cache[idx - 2] + cache[idx - 1]#compute fibonacci numbers

    return cache[num]
