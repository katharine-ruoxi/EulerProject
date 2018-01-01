# 007
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import math

'''
order = 1
number = 2
while order < 10001:
    number += 1 
    count =0
    for i in range(2,int(number/2)+1):
        if number % i == 0 :
            count += 1
        
    
    if count == 0:
        order +=1
    
print number
'''



prime=[2]
number = 2

while len(prime) < 10001:
    number +=1
    count = 0
    for i in range(len(prime)):
        if number % prime[i] == 0:
            count +=1
    if count == 0:
        prime.append(number)
print prime[-1]

