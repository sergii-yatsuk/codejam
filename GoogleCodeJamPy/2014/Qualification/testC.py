
__author__ = 'sergeyy'
import time

def solvSmal(r,c,m):
    if  r==2 or c ==2:
        raise NameError('\nImpossible')
    if max(r,c) - m > 2:
        if max(r,c) == r:
            mat = genEmpty(r, c-1)
            col = ['.']*(r-m)+['*']*m
            for row, coli in zip(mat, col):
                row.append(coli)
            return mat
        elif max(r,c) == c:
            mat = genEmpty(r-1, c)
            row = ['.']*(c-m)+['*']*m
            mat.append(row)
            return mat
    else:
        mid = m -1
        if max(r,c) == r:

            col = ['.']*(r-mid)+['*']*mid
            mat = solvSmal(r, c-1, m-mid)
            for row, coli in zip(mat, col):
                row.append(coli)
            return mat
        elif max(r,c) == c:

            row = ['.']*(c-mid)+['*']*mid
            mat = solvSmal(r-1, c, m-mid)
            mat.append(row)
            return mat



def genEmpty(r,c):
    mat = []
    for i in range(r):
        r = ['.']*c
        mat.append(r)

    mat[0][0]='c'
    return mat

def solvEmty(r,c, prev):
    if r==1 and c == 1:
        return [['c']]
    #if r==1 and c ==2 or\
    #    r==2 and c ==1:
    #    return genEmpty(r,c)
    if c==1 and prev == 'c' or \
       r==1 and prev == 'r':
        raise NameError('\nImpossible')
    return genEmpty(r,c)


def solve(r,c,m, prev):
    if m >= min(r,c):
        if min(r,c) == r:
            mat = solve(r, c-1, m-r, 'c')
            for row in mat:
                row.append('*')
            return mat
        elif min(r,c) == c:
            mat = solve(r-1, c, m-c, 'r')
            appendRow = ['*']*c
            mat.append(appendRow)
            return mat
    elif m == 0:
        return solvEmty(r,c, prev)
    else:
        mat = solvSmal(r,c,m)
        return mat

def printMat(mat):
    out = '\n'
    for row in mat:
        out = out + ''.join(row) + '\n'
    out = out[:-1:]
    return out


def check(r, c, m):
    #if r*c -m ==1:
    #    return '\nImpossible'
    try:
        return printMat(solve(r,c,m,''))
    except NameError as ex:
        return str(ex)

case = 1
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            line = fin.readline()
            rcm = line[:-1:].split(' ')
            R = int(rcm[0])
            C = int(rcm[1])
            M = int(rcm[2])

            oline = ''
            oline = 'Case #' + str(i) +':' + check(R, C, M) +'\n'
            fout.write(oline)

#print (time.clock())



