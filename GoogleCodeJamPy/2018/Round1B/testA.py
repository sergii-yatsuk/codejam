__author__ = 'sergii'


import sys

name = "A-small-practice"
path = ""



fin = sys.stdin
fout = sys.stdout

fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")

N = 0
L = 0
v = []

def getRoundSum(a):
    r = 0
    for i in a:
        r = r + round(100*i/N)
    return r

def addToMin(v):
    a = v[:]
    
    b = [round(100*i/N) - 100*i/N for i in a]
    
    mi = 0
    for i in range(len(b)):
        if (b[i]>b[mi]):
            mi=i
        
    a[mi] = a[mi] + 1
    return a
    

def check(v):

        
    s = sum(v)

    while (s<N):
        b1 = v + [1]
        b2 = addToMin(v)
        
        if (getRoundSum(b1) > getRoundSum(b2)):
            v = b1
        else:
            v = b2
        s = s + 1
        

    return str(getRoundSum(v))
    


cnt = int(fin.readline())
for i in range(1, cnt+1):
    waffle = []
    line = fin.readline().split()
    N = int(line[0])
    L = int(line[1])
    v = [int(i) for i in fin.readline().split() ]
    fout.write('Case #' + str(i) +': ' + check(v) +'\n')
    fout.flush()
