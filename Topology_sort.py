'''
Basic topology sort.
It prints out the sorted values in the topology sort algorithm
'''

n = 7#0~6
graph = [[0, 1], [0, 3], [1, 2], [3, 4], [5, 6], [6, 4], [4, 2]]

adjlist = [[] for _ in range(n)]#to contain how each vertex is connected
indegrees = [0] * n#to contain each vertex's indegree

for i in graph:
    adjlist[i[0]].append(i[1])
    indegrees[i[1]] += 1

queue = []

for idx, indegree in enumerate(indegrees):
    if indegree == 0:
        queue.append(idx)

while queue:#till it has no value in it
    value = queue.pop(0)
    print(value)
    for i in adjlist[value]:
        indegrees[i] -= 1#decrease indegree
        if indegrees[i] == 0:
            queue.append(i)
