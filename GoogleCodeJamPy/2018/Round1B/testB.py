__author__ = 'sergii'


import sys

name = "B-small-practice"
path = ""



fin = sys.stdin
fout = sys.stdout

#fin = open(path + name + ".out")
#fout = open(path + name + ".out", "w")


s = 0
d = []
a = []
b = []
s1 = []
s2 =[]

def getLenth(ii):
    length = 0
    M = None
    N = None
   
    M=s1[ii]
    i = ii+1
    length = 1;
    while(True and i<s):
        if (s1[i]==M):
            length = length +1
            i = i +1
        elif (N is None):
            N = s2[i]
            i = i + 1
            length = length +1
        elif (s2[i]==N):
            length = length +1
            i = i + 1
        else:
            break;
    
    l1 = length
    
    M = None
    N = None
    N=s2[ii]
    i = ii+1
    length = 1;
    while(True and i<s):
        if (s2[i]==N):
            length = length +1
            i = i +1
        elif (M is None):
            M = s1[i]
            i = i + 1
            length = length +1
        elif (s1[i]==M):
            length = length +1
            i = i + 1
        else:
            break;
    
    l2 = length
        
    return max(l1, l2)


def check():
    y = 0
    z = 0
    
    for i in range(s):
        yy = getLenth(i)
        if (yy==y):
            z = z + 1
        elif (yy>y):
            y = yy
            z = 1
        
    return str(y)+" "+str(z)
    


cnt = int(fin.readline())
for test in range(1, cnt+1):
    s = int(fin.readline())
    d = []
    a = []
    b = []
    s1 = []
    s2 =[]
    for j in range(s):
        line =  fin.readline().split()
        d.append(int(line[0]))
        a.append(int(line[1]))
        b.append(int(line[2]))
        s1.append(d[-1]+a[-1])
        s2.append(d[-1]-b[-1])
    fout.write('Case #' + str(test) +': ' + check() +'\n')
    fout.flush()
