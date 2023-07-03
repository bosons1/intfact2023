#!/usr/bin/python3
import sys
from mpmath import *
from gmpy2 import *

def satisfies(degree, digit):
    f=open("./pi.txt", "r")
    g=open("./sqrt2.txt","r")
    c = 0
    f.read(2)
    g.read(2)
    pp = ""
    tt = ""
    while True:
        pp = str(f.read(1))
        tt = str(g.read(1))
        if pp == str(digit):
            c = c + 1
            if c == degree:
                break
    f.close()
    g.close()
    d = int(pp) + int(tt)
    if d == 1 or d == 11:
        return True
    else:
        return False

def divides(num, factor):
    fz = mpz(str(factor))
    nz = mpz(num)
    if fz <= 1:
        return False, ""
    rz = fmod(nz, fz)
    if rz == 0:
        qz = fdiv(nz, fz)
        return True, str(qz)
    else:
        return False, ""

num=str(sys.argv[1])
l = len(num)
zero_index = 1
mp.prec=27
mp.dps=27
i = 0
f=open("./pi.txt","r")
g=open("./sqrt2.txt","r")
f.read(2)
g.read(2)
while True:
   zero = str(zetazero(zero_index).imag)
   idx = zero.index(".")
   zero = zero[idx + 1:]
   zero = zero[:8]
   nn = num[l - 1 - i]
   i = (i + 1) % l
   hit = False
   zero_index = zero_index + 1
   for digit in zero:
       if digit == '0':
           digit = 10
       if not hit and satisfies(int(digit), int(nn)) == True:
           hit = True
   pp = str(f.read(1))
   tt = str(g.read(1))
   print([pp, tt])
   if hit == True:
       input("hit")
   print("")
f.close()
g.close()
