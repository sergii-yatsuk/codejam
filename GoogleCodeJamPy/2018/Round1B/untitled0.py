# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:19:27 2018

@author: Dell7520
"""

name = "B-small-practice"
path = ""

fout = open(path + name + ".out", "w")

x = 100000
fout.write(str(x)+'\n')


for i in range(x):
    fout.write(str(i)+" 0 "+str(i)+"\n")




fout.flush()