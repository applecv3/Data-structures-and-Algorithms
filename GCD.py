'''
Finding the greatest common divisor between 2 numbers.
'''


def gcd(a, b):

    while b != 0:
        r = a % b
        a = b
        b = r

    return a
