__author__ = 'sergii'


import sys
import time

name = "B-small-practice"
path = ""

fin = sys.stdin
fout = sys.stdout

fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")

          
def trouble_sort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L)-2):
            if L[i]>L[i+2]:
                done = False
                L[i], L[i+2] = L[i+2], L[i]
                
    return L

def find_bug(v):
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            return i
    return -1


def check(v):
    v = trouble_sort(v)
    print(v)
    b = find_bug(v)
    if b==-1:
        return "OK"
    else:
        return str(b)

cnt = int(fin.readline())
for i in range(1, cnt+1):
    n = int(fin.readline())
    v = [int(i) for i in fin.readline().split() ]
    fout.write('Case #' + str(i) +': ' + check(v) +'\n')
    # #fin.readline()
#print (time.clock())
    


