# 010
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math

mylist =[]


# check prime
def isPrime(number):  
    if number <= 1:  
        return 0
    for i in range(2, int(math.sqrt(number)) + 1):  
        if number % i == 0:  
            return 0
    return 1

# define numbers
for number in xrange(1,2000001):
    # store prime number into a list
    if isPrime(number) == 1:
        mylist.append(number)


# add numbers in the list 
result = sum(mylist)

# print the result 
print result