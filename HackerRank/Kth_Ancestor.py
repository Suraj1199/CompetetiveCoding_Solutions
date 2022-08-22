import math
class Graph:
    def __init__(self):
        self.edges={}
        self.root=None
    def add(self, node, parent):
        if parent==0:
            self.root=node
            self.edges[node]=[]
            return
        try:
            self.edges[parent].append(node)
            self.edges[node]=[]
        except:
            self.edges[parent]=[]
            self.edges[parent].append(node)
            self.edges[node]=[]
    def bfs_process(self, tree):
        tree.add(self.root, 0)
        self.bfs_helper(self.root, tree)
    def bfs_helper(self, root, tree):
        visited={x:False for x in self.edges.keys()}
        queue=[root]
        while len(queue)>0:
            create=[]
            for x in queue:
                for y in self.edges[x]:
                    if not visited[y]:
                        tree.add(y, x)
                        create.append(y)
                        visited[x]=True
            queue=create
class Tree:
    def __init__(self, p):
        self.root=None
        self.nodes=p
        self.parents={}
        self.level={}
    def add(self, node, parent):
        self.parents[node]=[]
        if parent==0:
            self.root=node
            self.level[node]=0
            return 
        self.parents[node].append(parent)
        level_list=self.parents[parent]
        level=0
        while len(level_list)>level:
            ll=level_list[level]
            self.parents[node].append(ll)
            level_list=self.parents[ll]
            level+=1
        self.level[node]=self.level[parent]+1
    def find(self, node, kth_parent):
        if node not in self.parents.keys():
            print(0)
            return
        if kth_parent>self.level[node]:
            print(0)
            return
        parent=0
        level_list=self.parents[node]
        while kth_parent>0:
            k=int(math.floor(math.log(kth_parent, 2)))
            parent=level_list[k]
            level_list=self.parents[parent]
            kth_parent=kth_parent-(2**k)
        print(parent)
    def delete(self, node):
        if node==self.root:
            self.root=None
        del self.parents[node]

test_cases=int(input())
for _0 in range(test_cases):
    p=int(input())
    t=Tree(p)
    g=Graph()
    root=None
    for _1 in range(p):
        x, y=list(map(int, input().split()))
        g.add(x, y)
    g.bfs_process(t)
    queries=int(input())
    for _2 in range(queries):
        l=list(map(int, input().split()))
        if l[0]==0:
            t.add(l[2], l[1])
        if l[0]==1:
            t.delete(l[1])
        if l[0]==2:
            t.find(l[1], l[2])
