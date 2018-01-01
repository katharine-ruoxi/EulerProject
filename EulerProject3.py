# 003
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
number = 600851475143

def factoring(number):
    isPrime = True
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i == 0:
            factor1 = i
            factor2 = number / i
            isPrime = False
            return [factor1] + factoring(factor2)
    if isPrime: return [number]


print max(factoring(number))