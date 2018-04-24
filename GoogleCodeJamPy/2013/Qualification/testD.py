__author__ = 'sergeyy'
import time
import math


def dfs(gr, u, path):
   path = path + [u]
   if not gr[u]:
      path.remove(u)
      print(path)
   for i in gr[u]:
      dfs(gr, i, path + gr[u])



def widthSearch(gr):
   path = []
   # for k in gr[0]:
   #    dfs(gr, k, path)
   dfs(gr, 0, path)

def findMin(keys,t):
   min = 1000000
   for k,v in t.items():
      if v[0] in keys and k < min:
         min =k
   return min


def buildNode(key, t):
   ret = list()
   for k,v in t.items():
      if v[0] == key:
         p = [k]
         if v[1::] != [0]:
            additionalKeys = list(v[2::])
            while additionalKeys:
               c = findMin(additionalKeys, t)
               nKey = t[c][0]
               additionalKeys.remove(nKey)
               if nKey != 0 :
                  add = buildNode(nKey, dict((k1,v) for k1,v in t .items() if k1!=k))
                  if add:
                     p.extend(add)

         ret.append(p)

   return ret


def solve(t, keys):
   gr ={}
   tree = []


   ret = list()
   for key in keys:
      add = buildNode(key, t)
      if add:
         ret.append(add)


   print(ret)
   #
   # for i in range(len(t)):
   #    cur = []
   #    for j in range(len(t)):
   #       if i!=j:
   #          if t[j][0] in t[i][2::]:
   #             gr[i+1] = gr.get(i+1,[]) + [j+1]
   #             cur.append(j+1)
   #
   #    # for k in cur:
   #    #    for k1 in cur:
   #    #       if k != k1:
   #    #          gr[k] = gr.get(k,[]) + [k1]
   #
   #
   # for k,v in gr.items():
   #    gr[k] = sorted(v, reverse=False)
   #
   # widthSearch(gr)
   return "IMPOSSIBLE"

time.clock()

with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         k, n = [int(x) for x in fin.readline().split()]
         keys = [int(x) for x in fin.readline().split()]
         t = {}
         for i in range(n):
            t[i+1] =  [int(x) for x in fin.readline().split()]

         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(t, keys) +'\n'
         fout.write(oline)
print (time.clock())




