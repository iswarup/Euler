"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

import math

def isPrime(number):
    for i in range(2,int(number//2)):
        if number % i == 0:
            return False
    return True


def getPrimeFactors(number):
    """Returns list of factors of n."""
    return (i for i in range(1,int(math.sqrt(number//2))) if number % i == 0 and isPrime(i))

    # results = []
    # for i in range(1,int(number//2)):
    #     if number % i == 0:
    #         results.append(i)

print(list(getPrimeFactors(600851475143))[-1])