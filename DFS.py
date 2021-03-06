"""
Basic Depth First Search algorithm with recursion.
It prints out the node it's visited in order.
"""


vertexList = [0, 1, 2, 3, 4]
edgeList = [(0, 1), (0, 4), (1, 0), (2, 3), (2, 4), (3, 2), (4, 0), (4, 2)]  # bidirected
adjlist = [[] for _ in vertexList]  # to organize the graph in list form
visited = [False] * 5  # to check if it's visited a certain vertex

for i in edgeList:
    adjlist[i[0]].append(i[1])


def dfs(vertex):
    visited[vertex] = True
    print(vertex)

    for neighbor in adjlist[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)


dfs(0)
