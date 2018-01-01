# 009
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math



for b in xrange(1,501):
    for a in xrange(1,b):
        c = math.sqrt(a**2+b**2)
        if a+b+c == 1000:
            print a*b*c
