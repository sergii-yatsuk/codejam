__author__ = 'sergeyy'
import time
import math


def isPalin(n):
   s = str(n)
   p = len(s)
   for i in range(int(p/2)):
      if s[i] != s[p-i-1]:
         return False
   return True
   # a = s[:math.floor(p):]
   # b = (s[math.ceil(p)::])[::-1]
   # return a==b


def solve(a, b):
   cnt = 0
   aa = math.ceil(math.sqrt(a))
   bb = math.floor(math.sqrt(b))
   for i in range(aa, bb+1):
      if isPalin(i) and isPalin(i*i):
         cnt = cnt+1
   return str(cnt)

time.clock()

with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         a, b = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(a,b) +'\n'
         fout.write(oline)
print (time.clock())




