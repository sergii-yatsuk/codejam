import time


def solve(a):

   for h in getUsedH(a):
      a = removeH(a,h)
      if a == False:
         return 'NO'

   if a:
      return 'NO'
   return 'YES'


with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         n, m = [int(x) for x in fin.readline().split()]
         a = [[]*m]*n
         for i in range(n):
            a[i] = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(a) +'\n'
         fout.write(oline)
print (time.clock())



