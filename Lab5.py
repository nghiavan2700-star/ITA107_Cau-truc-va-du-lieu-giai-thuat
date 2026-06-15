# Bài 1:

from collections import deque

def build_graph(edges, directed=False):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, [])
        graph.setdefault(v, [])
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return res

def dfs_recursive(graph, start, visited=None, res=None):
    if visited is None:
        visited = set()
    if res is None:
        res = []
    visited.add(start)
    res.append(start)
    for v in graph[start]:
        if v not in visited:
            dfs_recursive(graph, v, visited, res)
    return res

def count_connected_components(graph):
    visited = set()
    components = []

    def bfs_comp(start):
        q = deque([start])
        visited.add(start)
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return comp

    for u in graph:
        if u not in visited:
            components.append(bfs_comp(u))
    return len(components), components

edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]
print(build_graph(edges))
print(build_graph(edges, True))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS A:", bfs(graph, 'A'))
print("BFS D:", bfs(graph, 'D'))
print("DFS A:", dfs_recursive(graph, 'A'))
print("DFS C:", dfs_recursive(graph, 'C'))

graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['C'],
    'F': []
}
print(count_connected_components(graph2))

# Bài 2:

def has_cycle_undirected(graph):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for u in graph:
        if u not in visited:
            if dfs(u, None):
                return True
    return False

def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}

    def dfs(u):
        color[u] = GRAY
        for v in graph[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    for u in graph:
        if color[u] == WHITE:
            if dfs(u):
                return True
    return False

g1 = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
g2 = {0:[1,2], 1:[0,3], 2:[0], 3:[1]}
g3 = {0:[1], 1:[0], 2:[3,4], 3:[2,4], 4:[2,3]}

print(has_cycle_undirected(g1))
print(has_cycle_undirected(g2))
print(has_cycle_undirected(g3))

d1 = {0:[1], 1:[2], 2:[0]}
d2 = {0:[1,2], 1:[3], 2:[3], 3:[]}
d3 = {0:[1], 1:[2], 2:[3], 3:[1]}

print(has_cycle_directed(d1))
print(has_cycle_directed(d2))
print(has_cycle_directed(d3))

# Bài 3:

from collections import deque

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)

    for u in graph:
        if u not in visited:
            dfs(u)
    return stack[::-1]

def topological_sort_kahn(graph):
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([u for u in graph if indegree[u] == 0])
    res = []

    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return res if len(res) == len(graph) else None

def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for a, b in prerequisites:
        graph[b].append(a)
    return topological_sort_kahn(graph) is not None

def find_order(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for a, b in prerequisites:
        graph[b].append(a)
    order = topological_sort_kahn(graph)
    return order if order else []

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

print("DFS topo:", topological_sort_dfs(graph))
print("Kahn topo:", topological_sort_kahn(graph))

print(can_finish(4, [[1,0], [2,0], [3,1], [3,2]]))
print(can_finish(2, [[0,1], [1,0]]))

print(find_order(4, [[1,0], [2,0], [3,1], [3,2]]))
print(find_order(2, [[0,1], [1,0]]))