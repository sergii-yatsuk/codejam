__author__ = 'sergeyy'
import time
import math

def prebuild(m):
    ret = [0*m]
    for i in range(m):
        ret.append((i+1)**2-i**2)
        print((i+1)**2-i**2)
    return ret


def solve(E,R,v):
    ret = 0
    for i in range(len(v)-1):
        if v[i+1]*E < v[i]*E+v[i+1]*R:
            ret = ret + v[i]*E
            E = R
    ret = ret+ v[-1]*E
    return str(ret)




time.clock()
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         E,R,N = [int(x) for x in fin.readline().split()]
         v = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(E,R,v) +'\n'
         fout.write(oline)
print (time.clock())




