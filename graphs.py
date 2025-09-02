n = 4
graph = [[0]*n for i in range(n)]
graph[0][1] = 1
graph[0][2] = 1
graph[2][0] = 1
graph[1][3] = 1
graph[3][1] = 1
print("Adjacency Matrix: ")
for row in graph:
    print(row)