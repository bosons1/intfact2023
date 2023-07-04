#!/usr/bin/python3
from __future__ import print_function
import sys
from gmpy2 import *
MAGIC=10

def complement(num):
    c_num = ""
    for x in num:
        c = str((11 - int(x)) % 10)
        c_num = c_num + c
    return c_num

def characterize(num):
    global MAGIC
    c = 0
    f = open("./sqrt2.txt", "r")
    state_vec = []
    f.read(2)
    l = len(num)
    pos = 0
    while c < MAGIC*l:
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
l1 = len(state_vec1)
f=open("./sqrt2.txt","r")
f.read(2)
t=f.read(l1)
f.close()
f=open("./pi.txt","r")
f.read(2)
print(t)
print("\n")
print(f.read(l1))
print("\n")
g=open("./e.txt","r")
g.read(2)
print(g.read(l1)[::-1])
f.close()
g.close()
print("\n")
sys.exit(0)
c_num = complement(num)
state_vec2 = characterize(c_num)
f=open("./sqrt2.txt","r")
f.read(2)
for x in state_vec2:
    print([x, int(f.read(1))],end=',')
f.close()
print("\n")
f=open("./pi.txt","r")
f.read(2)
l2 = len(state_vec2)
print(f.read(l2))
g=open("./e.txt","r")
g.read(2)
print(g.read(l2)[::-1])
f.close()
g.close()
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
