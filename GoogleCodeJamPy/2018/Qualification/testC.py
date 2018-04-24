__author__ = 'sergii'


import sys

fin = sys.stdin

#fin = open("C-small-practice.in")

w, h = 1010, 1010;
orchard  = [[0 for x in range(w)] for y in range(h)] 
a = 0
rows = 5
cols = 4

def is_filed_3x3(row, col):
    
   
    for i in range(-1,2):
        for j in range(-1,2):
            if orchard[row+i][col+j]==0:
                return False;
    return True

def fill_3x3(row, col):
    if is_filed_3x3(row, col):
        return True;
    
    if row<rows and orchard[row-1][col-1] == orchard[row-1][col] == orchard[row-1][col+1] == 1:
        return fill_3x3(row+1, col)
    
    if col<cols and orchard[row-1][col-1] == orchard[row][col-1] == orchard[row+1][col-1] == 1:
        return fill_3x3(row, col+1)

    while not is_filed_3x3(row, col):
        print (row, col)
        sys.stdout.flush()
        line = fin.readline().split()
        x = int(line[0])
        y = int(line[1])
        #sys.stderr.write(" "+str(x)+" " + str(y))
        if x==-1 and y==-1:
            #sys.stderr.write("-1 -1\n")
            return False
        if x==0 and y==0: 
            #sys.stderr.write("0 0\n")
            return False
        orchard[x][y] = 1
        
    return True

t = int(fin.readline())

for i in range(1, t+1):
    a = int(fin.readline())
    orchard  = [[0 for x in range(w)] for y in range(h)] 
    
    if (a == 20):
        rows = 5
        cols = 4
        if (fill_3x3(3,3)):
            if (fill_3x3(3,4)):
                if(fill_3x3(5,3)):
                    fill_3x3(5,4)
    else:
        cont = True
        rows = 10
        cols = 20
        for i in [3,5,7,9,10]:
            for j in [3,5,7,9,11,13,15,17,19,20]:
                if cont:
                    cont = fill_3x3(i,j)
       
    





