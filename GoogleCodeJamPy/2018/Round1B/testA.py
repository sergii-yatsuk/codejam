__author__ = 'sergii'


import sys

name = "A-small-practice"
path = ""



fin = sys.stdin
fout = sys.stdout

#fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")


waffle  = []
R = 0
C = 0
H = 0
V = 0


def checkPice(x1,y1, x2,y2, chipsPerPiese):
    total = 0
    
    for i in range(x1,x2):
        for j in range(y1,y2):
            if waffle[j][i]=='@':
                total = total +1
    
    return total==chipsPerPiese


def check():
    hor = []
    ver = []
    totalChips = 0
    for row in waffle:
        totalChips = totalChips + row.count('@')
    
    if totalChips == 0:
        return "POSSIBLE"
    
    pices = (H+1)*(V+1)
   
    if totalChips % pices != 0:
        return "IMPOSSIBLE" 

    chipsPerPiese = totalChips//pices
    
    if totalChips % (H+1) != 0:
        return "IMPOSSIBLE" 
    
    chipsPerRow = totalChips//(H+1)
    
    if totalChips % (V+1) != 0:
        return "IMPOSSIBLE" 
    
    chipsPerCol = totalChips//(V+1)
    
    chips = 0
    i = 0
    while i < R:
        while chips<chipsPerRow and i <R:
            chips = chips + waffle[i].count('@')
            i = i +1
        if chips>chipsPerRow or i >R:
            return "IMPOSSIBLE" 
        chips = 0
        if (len(hor)<H+1):
            hor.append(i)
        else:
            return "IMPOSSIBLE"  
    
    if len(hor) != H+1:
        return "IMPOSSIBLE"  
    
    chips = 0
    j = 0
    while j < C:
        while chips<chipsPerCol and j < C:
            for row in waffle:
                if row[j] == '@':
                    chips = chips + 1
            j = j + 1
        if chips>chipsPerCol or j>C:
            return "IMPOSSIBLE" 
        chips = 0
        if (len(ver)<V+1):
            ver.append(j)
        else:
            return "IMPOSSIBLE"  
        
    if len(ver) != V+1:
        return "IMPOSSIBLE"  
    
    
    hor = [0] + hor
    ver = [0] + ver

    for i in range(H+1):
        for j in range(V+1):
            if not checkPice(ver[j],hor[i],ver[j+1],hor[i+1], chipsPerPiese):
                return "IMPOSSIBLE"
            
    
    return "POSSIBLE"
    


cnt = int(fin.readline())
for i in range(1, cnt+1):
    waffle = []
    line = fin.readline().split()
    R = int(line[0])
    C = int(line[1])
    H = int(line[2])
    V = int(line[3])
    for j in range(R):
        waffle.append(fin.readline().strip())
    fout.write('Case #' + str(i) +': ' + check() +'\n')
    fout.flush()
