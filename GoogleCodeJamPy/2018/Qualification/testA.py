__author__ = 'sergii'


import sys

name = "A-small-practice"
path = ""



fin = sys.stdin
fout = sys.stdout

#fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")

def get_cur_damage(p):
    cur_power = 1
    cur_damage = 0
    for c in p:
        if c=='S':
            cur_damage+=cur_power
        else:
            cur_power *= 2
    return cur_damage


def decrease_damage(p):
    i = p.rfind("CS")
    p = p[:i] + "SC" + p[i+2:]
    return p

def check(d, p):
    s = p.count('S')

    if (s>d):
        return "IMPOSSIBLE"
    cur_damage = get_cur_damage(p)
    
    if cur_damage <= d:
        return "0"
    cntr = 0
    while cur_damage>d:
        p = decrease_damage(p)
        cur_damage = get_cur_damage(p)
        cntr += 1
    return str(cntr)


cnt = int(fin.readline())
for i in range(1, cnt+1):
    line = fin.readline().split()
    d = int(line[0])
    p = line[1]
    fout.write('Case #' + str(i) +': ' + check(d, p) +'\n')
    # #fin.readline()
#print (time.clock())



