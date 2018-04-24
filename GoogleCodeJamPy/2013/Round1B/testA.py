__author__ = 'sergeyy'
import time
import math

def prebuild(m):
    ret = [0*m]
    for i in range(m):
        ret.append((i+1)**2-i**2)
        print((i+1)**2-i**2)
    return ret


def solve(a, r, add):
    for i in range(len(r)):
        if r[i] < a:
            a = a+r[i]
        elif
    return add

time.clock()
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         a, n = [int(x) for x in fin.readline().split()]
         r = [int(x) for x in fin.readline().split()]
         r = sorted(r)
         oline = ''
         oline = 'Case #' + str(case) +': ' + str(solve(a,r, 0)) +'\n'
         fout.write(oline)
print (time.clock())




