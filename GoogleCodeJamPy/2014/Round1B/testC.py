
__author__ = 'sergeyy'
import time
import copy
import itertools


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def isPossibleDest(dst, r, routes, toUse):
    used = r[:dst-1]
    i = r[dst-1]
    j = r[dst]

    if j in routes.get(i, []):
        toUse.append((j, i))
        return True

    used.append(i)
    used.append(j)

    curRoutes = dict((k, [x for x in v if x in used]) for (k, v) in routes.items() if k in used)

    for i in range(len(used)-1):
        l = curRoutes.get(used[i], [])
        if used[i+1] in l:
            curRoutes[used[i]].remove(used[i+1])


    p = find_path(curRoutes, i , j)

    if p is None:
        return False
    else:
        for i in range(len(p)-1):
            if (p[i], p[i+1]) in toUse:
                toUse.remove((p[i], p[i+1]))
            else:
                toUse.append((p[i+1], p[i]))

        return True




def isPossibleRoute(r, routes):
    toUse = []
    for i in range(1, len(r)):

        if not isPossibleDest(i,r, routes, toUse):
            return False

    p = find_path(routes, r[-1] , r[0])

    if p is None:
        return False
    else:
        for i in range(len(p)-1):
            if (p[i], p[i+1]) in toUse:
                toUse.remove((p[i], p[i+1]))
            else:
                toUse.append((p[i+1], p[i]))


    print(r)
    print(toUse)
    return True

def check(n, m ,zips, routes):
    keys = [i for i in zips.keys()]
    keys.sort()
    for p in itertools.permutations(keys):
        r = []
        for i in p:
            r.append(zips[i])

        if isPossibleRoute(r, routes):
            return ''.join(p)

    return ''.join(zips.keys())

case = 1
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            zips = {}
            routes = {}
            line = fin.readline()
            nm = line[:-1:].split(' ')
            n = int(nm[0])
            m = int(nm[1])
            for j in range(n):
                line = fin.readline().strip()
                zips[line] = j+1
            for j in range(m):
                line = fin.readline()
                pp = line[:-1:].split(' ')
                routes.setdefault(int(pp[0]), []).append(int(pp[1]))
                routes.setdefault(int(pp[1]), []).append(int(pp[0]))



            oline = ''
            oline = 'Case #' + str(i) +': ' + check(n, m ,zips, routes) +'\n'
            fout.write(oline)

#print (time.clock())



