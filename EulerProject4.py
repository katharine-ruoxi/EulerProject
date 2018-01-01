# 004
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 
9009 = 91 * 99.
Find the largest palindrome made from the product of 
two 3-digit numbers.

'''

e = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        a = i * j
        b = str(a)
        c = len(b)
        d = 0
        for k in range(0,c):
            if b[k] == b[c-k-1]:
                d += 1
            if d == c:
                if e < a:
                    e = a 

print e