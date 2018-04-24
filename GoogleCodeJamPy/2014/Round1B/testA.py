
__author__ = 'sergeyy'
import time


def check(a, b, k):
    cnt = 0
    for i in range(a):
        for j in range(b):
            if (i&j)<k:
                cnt+=1
    return str(cnt)

case = 1

time.clock()

with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            line = fin.readline()
            rcm = line[:-1:].split(' ')
            A = int(rcm[0])
            B = int(rcm[1])
            K = int(rcm[2])

            oline = ''
            oline = 'Case #' + str(i) +': ' + check(A, B, K) +'\n'
            fout.write(oline)
            #fin.readline()
print (time.clock())



