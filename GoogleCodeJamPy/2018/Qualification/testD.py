__author__ = 'sergii'


import sys
import time
import math

name = "D-small-practice"
path = ""

fin = sys.stdin
fout = sys.stdout

#fin = open(path + name + ".in")
#fout = open(path + name + ".out", "w")


def check(a):
    if a > 1.414213:
        a = 0.5
        return "{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}".format(a, a,a,a,a,a, a,a, a)
    if a == 1.0:
        return "{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}".format(0.5, 0,0, 0, 0.5, 0, 0,0,0.5)
    
    ab = 0.5
    ac = math.sqrt(2)/2
    ad = a/2
    cd = math.sqrt(ac*ac-ad*ad)
    alpha = abs(math.asin(cd/ac))
    
    beta = math.pi/4 - alpha
    ob = ab*math.sin(beta)
    ao = math.sqrt(ab*ab-ob*ob)
    return "{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}\n{:.8f} {:.8f} {:.8f}".format(ao, ob,0, -ob, ao, 0, 0,0,0.5)

cnt = int(fin.readline())
for i in range(1, cnt+1):
    a = float(fin.readline())
    fout.write('Case #' + str(i) +':\n' + check(a) +'\n')
    # #fin.readline()
#print (time.clock())
    


