# method 1 - using kruskal algotithm

class DisjointSet(dict):    
    # dictionary
    ### child : parent

    # to add seperate n MSTs with 1 node in each
    def add(self,item):
        self[item] = item

    def find(self,item):
        parent = self[item]
        while self[parent] != parent:
            parent = self[parent]
        self[item] = parent 
        return parent
        
    def union(self, item1, item2):
        ###
        # I'm not changing self[item1] 
        # self[item1] is the point where the while loop stop in "def find"
        self[item2] = self[item1]

def kruskal (edges,l):  # l = number of nodes

    MST = []    # minimum spaining tree

    forest = DisjointSet()
    for i in range(l):
        forest.add (i)
    l -= 1
    for e in edges:
        n1,n2 = e[1],e[2]       # node 1 , node 2
        t1 = forest.find (n1)   # temp node 1
        t2 = forest.find (n2)   # temp node 2
        if t1 != t2:
            MST.append(e)
            l -= 1
            if l == 0:
                return MST
            forest.union(t1,t2)     # t1 > t2

N,M = map(int,input().split())
edges = []
for i in range(M):
    e1, e2, w = map(int,input().split())
    edges.append([w,e1-1,e2-1])
edges.sort()

originalWeight = sum(int(i[0]) for i in edges)

MST = kruskal(edges,N)
newWeight = sum(int(i[0]) for i in MST)

print(newWeight)
