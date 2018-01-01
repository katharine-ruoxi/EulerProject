# 005
'''
2520 is the smallest number that can 
be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
 of the numbers from 1 to 20?
'''
flag = True 
number = 20
while flag == True:
    count = 0
    for i in range(2,21):
        if number % i == 0:
            count += 1
    if count == 19:
        flag == False
        print number
        exit()
    else:
        number += 1