'''
Finding prime numbers with 'Sieve of Eratosthenes' algorithm.
Set an initial number and find all the prime numbers smaller than the initial number.
'''


def sieve(n):

    prime_numbers = []
    isprime = [False] * 2 + [True] * (n-1)  # set as 'True' at first from '2'

    for start in range(2, n+1):

        if isprime[start]:

            prime_numbers.append(start)

            for j in range(start*2, n+1, start):

                isprime[j] = False  # erasing non prime numbers

    return prime_numbers


print(sieve(15))
