__author__ = 'sergeyy'
import time
import math
import random

def check(p, a):
    if p[0]*p[0]*p[0] or \
       p[0]*p[0]*p[1] or \
       p[0]*p[0]*p[2] or\
       p[0]*p[1]*p[0] or\
       p[0]*p[1]*p[1] or\
       p[0]*p[1]*p[2] or\
       p[0]*p[0]*p[0] or\
       p[0]*p[0]*p[1] or\
       p[0]*p[0]*p[2] or\
       p[0]*p[2]*p[0] or\
       p[0]*p[2]*p[1] or\
       p[0]*p[2]*p[2] or\
       p[1]*p[0]*p[0] or\
       p[1]*p[0]*p[1] or\
       p[1]*p[0]*p[2] or\
       p[1]*p[1]*p[0] or\
       p[1]*p[1]*p[1] or\
       p[1]*p[1]*p[2] or\
       p[1]*p[0]*p[0] or\
       p[1]*p[0]*p[1] or\
       p[1]*p[0]*p[2] or\
       p[1]*p[2]*p[0] or\
       p[1]*p[2]*p[1] or\
       p[1]*p[2]*p[2] or\
       p[2]*p[0]*p[0] or\
       p[2]*p[0]*p[1] or\
       p[2]*p[0]*p[2] or\
       p[2]*p[1]*p[0] or\
       p[2]*p[1]*p[1] or\
       p[2]*p[1]*p[2] or\
       p[2]*p[0]*p[0] or\
       p[2]*p[0]*p[1] or\
       p[2]*p[0]*p[2] or\
       p[2]*p[2]*p[0] or\
       p[2]*p[2]*p[1] or\
       p[2]*p[2]*p[2] or\
       p[1]*p[1]*p[1]:
        return True


def solve(R, N, M, K, a):
    ret = '\n'
    for i in range(R):
        br = True
        while br:
            p = []
            for j in range(N):
                p.append(random.randrange(2,M+1))
            if check(p, a[i]):
                br = False
        ret = ret + ''.join([str(x) for x in p])+'\r'
    return str(ret)




time.clock()
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         R, N, M, K = [int(x) for x in fin.readline().split()]
         a = {}
         for i in range(R):
            a[i] = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(R, N, M, K,a) +'\n'
         fout.write(oline)
print (time.clock())




