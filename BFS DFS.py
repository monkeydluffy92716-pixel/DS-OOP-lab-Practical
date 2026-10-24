from collections import deque

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(vertices)

edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'E'), ('C', 'F')
]

# Adjacency matrix for DFS
matrix = [[0] * n for _ in range(n)]

# Adjacency list for BFS
adj_list = {v: [] for v in vertices}

for u, v in edges:
    i = vertices.index(u)
    j = vertices.index(v)

    matrix[i][j] = 1
    matrix[j][i] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)

# DFS using adjacency matrix
def dfs(start):
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)
        i = vertices.index(vertex)

        for j in range(n):
            if matrix[i][j] == 1:
                neighbor = vertices[j]
                if neighbor not in visited:
                    visit(neighbor)

    visit(start)
    return result

# BFS using adjacency list
def bfs(start):
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

print("Adjacency Matrix:")
for row in matrix:
    print(row)

print("\nAdjacency List:")
for vertex in adj_list:
    print(vertex, ":", adj_list[vertex])

print("\nDFS Traversal:", dfs('A'))
print("BFS Traversal:", bfs('A'))