# method 1 - using kruskal algotithm
def convertToEdges(m):
    e = []
    l = len(m)
    for r in range(l):
        for c in range(r):              # to get edges without repeating
            if m[r][c] != '-':
                e.append([int(m[r][c]),r,c])     # [ weight , raw , column ]
    e.sort()
    return e

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

m = []
f = open ("C:/Users/DELL/Desktop/Python (Euler)/107 Project Euler.txt", "r")
for line in f.read().split ('\n'):
    m.append (line.split (","))
f.close()

edges = convertToEdges (m)
originalWeight = sum(int(i[0]) for i in edges)

MST = kruskal(edges,len(m))
newWeight = sum(int(i[0]) for i in MST)

print("Original Weight = ",originalWeight)
print("New Weight      = ",newWeight)
print("Maximum saving  = ",originalWeight-newWeight)
