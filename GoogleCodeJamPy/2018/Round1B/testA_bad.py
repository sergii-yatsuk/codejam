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

def check():
    result = 0;
        
    i = 0;
    s = sum(v)

    while (s<N):
        ii = None
        for i in range(len(v)):
            if (round(100*v[i]/N) - 100*v[i]/N <= 0):
                ii = i
                break
        if ii is None:
            v.append(1)
            s = s + 1
        else:
            v[ii] = v[ii] + 1
            s = s +1
             
    for i in v:
        result = result + round(100*i/N)
    return str(result)
    


cnt = int(fin.readline())
for i in range(1, cnt+1):
    waffle = []
    line = fin.readline().split()
    N = int(line[0])
    L = int(line[1])
    v = [int(i) for i in fin.readline().split() ]
    fout.write('Case #' + str(i) +': ' + check() +'\n')
    fout.flush()
