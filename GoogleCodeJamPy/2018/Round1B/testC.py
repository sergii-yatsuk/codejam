__author__ = 'sergii'


import sys

name = "C-small-practice"
path = ""



fin = sys.stdin
fout = sys.stdout

fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")

M = 0
R = []
G = []
used = []

def gogo(i, used):
    
    if (R[i][0] == 0 or R[i][1] == 0):
        return;
        
    m = min(G[R[i][0]], G[R[i][1]])
    if (m==0):
        return
    
    if (G[R[i][0]] == m):
        if (R[i][0] in used):
            m = m // 2
    else:
        if (R[i][1] in used):
            m = m // 2
    if (m==0):
        return
    used.append(R[i][0])    
    used.append(R[i][1])
    G[i] = G[i] + m

    G[R[i][0]] = G[R[i][0]] - m 
    G[R[i][1]] = G[R[i][1]] - m
    
    gogo(R[i][0], used)
    gogo(R[i][1], used)

def check():
    prev = -1
    while (prev != G[0]):
        used = []
        gogo(0, used)
        prev = G[0] 
    return str(G[0])
    


cnt = int(fin.readline())
for i in range(1, cnt+1):
    M = int(fin.readline())
    for i in range(M):
        line = fin.readline().split()
        R.append((int(line[0])-1, int(line[1])-1))
    G = [int(i) for i in fin.readline().split() ]
    fout.write('Case #' + str(i) +': ' + check() +'\n')
    fout.flush()
