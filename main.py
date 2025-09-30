#bfs
from collections import deque
def bfs(t,s):
    v,q=[],deque([s])
    while q:
        n=q.popleft()
        if n not in v:v.append(n);q+=t[n]
    return v

t={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Children of {x}: ").replace(" ","")
    t[x]=c.split(",") if c else []
s=input("Start: ")
print("BFS Traversal:"," → ".join(bfs(t,s)))



#dfs
def dfs(t,s,v=None):
    if v is None:v=[]
    v.append(s)
    for c in t.get(s,[]):
        if c not in v:dfs(t,c,v)
    return v

t={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Children of {x}: ").replace(" ","")
    t[x]=c.split(",") if c else []
s=input("Start: ")
print("DFS Traversal:"," → ".join(dfs(t,s)))



#ucs
import heapq
def ucs(g,s,e):
    if s==e:return [s],0
    q=[(0,s,[s])];v=set()
    while q:
        c,n,p=heapq.heappop(q)
        if n==e:return p,c
        if n not in v:
            v.add(n)
            for nb,w in g.get(n,[]): 
                if nb not in v:heapq.heappush(q,(c+w,nb,p+[nb]))
    return None,None

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");es=input(f"Edges from {x} (n:w,...): ").replace(" ","")
    g[x]=[(a,int(b)) for a,b in (e.split(":") for e in es.split(","))] if es else []
s=input("Start: ");e=input("Goal: ")
p,c=ucs(g,s,e)
if p:print("Path found:"," → ".join(p));print("Total cost:",c)
else:print("No path found.")




#dls
def dls(g,c,t,d,v=None):
    if v is None:v=[]
    v.append(c)
    if c==t:return v
    if d<=0:return
    for nb in g.get(c,[]):
        if nb not in v:
            p=dls(g,nb,t,d-1,v.copy())
            if p:return p

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Children of {x}: ").replace(" ","")
    g[x]=c.split(",") if c else []
s=input("Start: ");t=input("Goal: ");d=int(input("Depth limit: "))
r=dls(g,s,t,d)
print("Path found:"," → ".join(r) if r else "No path found within depth limit")



#ids
def dls(g,c,t,d,v):
    if c==t:return [c]
    if d<=0:return
    v.append(c)
    for nb in g.get(c,[]):
        if nb not in v:
            p=dls(g,nb,t,d-1,v.copy())
            if p:return [c]+p

def ids(g,s,t,m):
    for d in range(m+1):
        p=dls(g,s,t,d,[])
        if p:return p

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Children of {x}: ").replace(" ","")
    g[x]=c.split(",") if c else []
s=input("Start: ");t=input("Goal: ");m=int(input("Max depth: "))
r=ids(g,s,t,m)
print("Path found:" if r else "No path found within depth limit", " → ".join(r) if r else "")



#bds
from collections import deque
def step(g,q,v,o):
    if q:
        c=q.popleft()
        for nb in g.get(c,[]):
            if nb not in v:
                v.add(nb);q.append(nb)
                if nb in o:return nb

def bidi(g,s,t):
    if s==t:return {s},{t},s
    vs,vg={s},{t};qs,qg=deque([s]),deque([t])
    while qs and qg:
        m=step(g,qs,vs,vg)
        if m:return vs,vg,m
        m=step(g,qg,vg,vs)
        if m:return vs,vg,m
    return None,None,None

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Neighbors of {x}: ").replace(" ","")
    g[x]=c.split(",") if c else []
s=input("Start: ");t=input("Goal: ")
vs,vg,m=bidi(g,s,t)
if m:
    print("Search met at:",m)
    print("Start side visited:"," → ".join(vs))
    print("Goal side visited:"," → ".join(vg))
else:print("No path found.")




#gbfs
import heapq
def gbfs(g,s,t,h):
    q=[(h[s],s)];v=set();p={s:None}
    while q:
        _,c=heapq.heappop(q)
        if c==t:
            r=[]
            while c:r.append(c);c=p[c]
            return r[::-1]
        v.add(c)
        for nb in g.get(c,[]):
            if nb not in v:
                p[nb]=c;heapq.heappush(q,(h[nb],nb))

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");c=input(f"Neighbors of {x}: ").replace(" ","")
    g[x]=c.split(",") if c else []
h={};print("Enter heuristic values:")
for x in g:h[x]=int(input(f"h({x}): "))
s=input("Start: ");t=input("Goal: ")
r=gbfs(g,s,t,h)
print("Path found:" if r else "No path found.", " → ".join(r) if r else "")



#a*
import heapq
def astar(g,s,t,h):
    q=[(h[s],0,s)];p={s:None};gc={s:0};v=set()
    while q:
        f,c,u=heapq.heappop(q)
        if u==t:
            r=[]
            while u:r.append(u);u=p[u]
            return r[::-1]
        v.add(u)
        for nb,w in g.get(u,[]):
            ng=gc[u]+w
            if nb not in v or ng<gc.get(nb,float('inf')):
                p[nb]=u;gc[nb]=ng
                heapq.heappush(q,(ng+h[nb],ng,nb))

g={};n=int(input("Nodes: "))
for _ in range(n):
    x=input("Node: ");es=input(f"Edges from {x} (n:w,...): ").replace(" ","")
    g[x]=[(a,int(b)) for a,b in (e.split(":") for e in es.split(","))] if es else []
h={};print("Enter heuristic values:")
for x in g:h[x]=int(input(f"h({x}): "))
s=input("Start: ");t=input("Goal: ")
r=astar(g,s,t,h)
print("Path found:" if r else "No path found.", " → ".join(r) if r else "")
