#!/usr/bin/python3
import sys
from gmpy2 import *

def complement(num):
    c_num = ""
    for x in num:
        c = str((11 - int(x)) % 10)
        c_num = c_num + c
    return c_num

def characterize(num):
    c = 0
    f = open("./sqrt2.txt", "r")
    state_vec = []
    f.read(2)
    l = len(num)
    pos = 0
    while c < l:
        s = str(f.read(1))
        d = int(s) + int(num[pos % l])
        if d == 11 or d == 1:
            state_vec.append(1)
            c = c + 1
        else:
            state_vec.append(0)
        pos = pos + 1
    f.close()
    return state_vec

num=str(sys.argv[1])
l = len(num)
state_vec1 = characterize(num)
c_num = complement(num)
state_vec2 = characterize(c_num)
print(len(state_vec1), len(state_vec2))
"""
factor1 = factorize(state_vec1)
factor2 = factorize(state_vec2)
dec1 = int(factor1, 2)
dec2 = int(factor2, 2)
if dec1*dec2 == num:
    print(num + " = " + str(dec1) + " X " + str(dec2))
else:
    print(num + " is a Prime Number.")
    """
