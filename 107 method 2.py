### method 2 - using Prim's Algorithm in Python 

# creating graph by adjacency matrix method
G = []
f = open ("C:/Users/DELL/Desktop/Python (Euler)/107 Project Euler.txt", "r")
for line in f.read().split ('\n'):
    G.append (line.split (","))
f.close()

V = len(G)      # number of vertices in graph
w = 0      # original Weight
for i in range(V):
    for j in range(V):
        if G[i][j] == '-':
            G[i][j] = 0
        else:
            G[i][j] = int(G[i][j])
            if i>j:
                w += G[i][j]        # calculate the original weight

INF = 999_999_999
MST = 0         # weight of MST

selected_node = [0 for i in range(len(G))]

no_edge = 0     # starting vertex
selected_node[no_edge] = True

# printing for edge and weight
#print("\nEdge \t: Weight")
while (no_edge < V - 1):
    
    minimum = INF
    a = 0
    b = 0
    for v in range(V):
        if selected_node[v]:
            for i in range(V):
                if ((not selected_node[i]) and G[v][i]):  
                    # not in selected and there is an edge
                    if minimum > G[v][i]:
                        minimum = G[v][i]
                        a = v
                        b = i
    #print(str(a) + "-" + str(b) + "\t: " + str(G[a][b]))
    MST += G[a][b]
    selected_node[b] = True
    no_edge += 1

print("original Weight  = ",w)
print("New weight       = ", MST)
print("Maximum saving   = ",w-MST)
