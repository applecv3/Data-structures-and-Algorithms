"""
Basic Breadth First Search algorithm with a queue
It prints out the node it's visited in order.
"""

import collections

vertexList = [0, 1, 2, 3, 4]
edgeList = [(0, 1), (0, 4), (1, 0), (2, 3), (2, 4), (3, 2), (4, 0), (4, 2)]  # bidirected
adjlist = [[] for _ in vertexList]  # organize the graph in list form
visited = [False] * 5  # to check if it's visited a certain vertex


for i in edgeList:
    adjlist[i[0]].append(i[1])


def bfs(start):
    queue = collections.deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current_item = queue.popleft()#deque
        for neighbor in adjlist[current_item]:
            if not visited[neighbor]:
                queue.append(neighbor)#enque all the neighbors
                visited[neighbor] = True
        print(current_item)


bfs(0)
