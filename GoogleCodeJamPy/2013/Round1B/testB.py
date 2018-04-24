__author__ = 'sergeyy'
import time
import math

def prebuild(m):
    ret = [0*m]
    for i in range(m):
        ret.append((i+1)**2-i**2)
        print((i+1)**2-i**2)
    return ret


def solve(n ,x ,y):
    a1 = 2*r+1
    D = (4-2*a1)**2+32*t
    x = ((4-2*a1)+math.sqrt(D))/8

    if x > 0:
        return str(int(x))
    return str(1)

    # ret = 0
    # while t>=0:
    #     p = 2*r+1
    #     r = r +2
    #     t = t - p
    #     ret = ret +1
    # return str(ret -1)


time.clock()
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         n, x, y = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(n ,x ,y) +'\n'
         fout.write(oline)
print (time.clock())




