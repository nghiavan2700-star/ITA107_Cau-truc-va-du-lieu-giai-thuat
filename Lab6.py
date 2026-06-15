# Bài 1:

import heapq

def dijkstra(graph, source):
    distances = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    distances[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, parent

def reconstruct_path(parent, source, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path if path and path[0] == source else None

def print_distances(distances, source):
    print(f"Bảng khoảng cách từ {source}:")
    for v in sorted(distances):
        d = distances[v]
        if d == float('inf'):
            print(f"{source} -> {v}: INF")
        else:
            print(f"{source} -> {v}: {d}")

def test_dijkstra():
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }

    source = 'A'
    distances, parent = dijkstra(graph, source)

    print_distances(distances, source)
    print("\nĐường đi chi tiết:")
    for v in sorted(graph):
        if v != source:
            path = reconstruct_path(parent, source, v)
            if path:
                print(f"{source} -> {v}: {' -> '.join(path)} (cost = {distances[v]})")
            else:
                print(f"{source} -> {v}: không có đường đi")

if __name__ == "__main__":
    test_dijkstra()

# Bài 2:

def make_set(vertices):
    return {v: v for v in vertices}

def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a

def make_set_optimized(vertices):
    parent = {v: v for v in vertices}
    size = {v: 1 for v in vertices}
    return parent, size

def find_optimized(parent, v):
    if parent[v] != v:
        parent[v] = find_optimized(parent, parent[v])
    return parent[v]

def union_optimized(parent, size, a, b):
    root_a = find_optimized(parent, a)
    root_b = find_optimized(parent, b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]

def demo_dsu_basic():
    vertices = ['A', 'B', 'C', 'D', 'E']
    parent = make_set(vertices)

    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E')
    ]

    for op in ops:
        if op[0] == "union":
            _, x, y = op
            print(f"union({x}, {y})")
            union(parent, x, y)
        else:
            _, x = op
            print(f"find({x}) = {find(parent, x)}")
        print("parent:", parent)

def demo_dsu_optimized():
    vertices = list(range(10))
    parent, size = make_set_optimized(vertices)

    for i in range(9):
        union_optimized(parent, size, i, i + 1)

    print("Trước find:", parent)
    for i in vertices:
        find_optimized(parent, i)
    print("Sau find:", parent)
    print("size:", size)

if __name__ == "__main__":
    demo_dsu_basic()
    print()
    demo_dsu_optimized()

# Bài 3:

def kruskal_mst_basic(vertices, edges):
    parent = make_set(vertices)
    mst = []
    total_weight = 0

    for w, u, v in sorted(edges):
        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            total_weight += w
            union(parent, u, v)

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight

def kruskal_mst_optimized(vertices, edges):
    parent, size = make_set_optimized(vertices)
    mst = []
    total_weight = 0

    for w, u, v in sorted(edges):
        if find_optimized(parent, u) != find_optimized(parent, v):
            mst.append((u, v, w))
            total_weight += w
            union_optimized(parent, size, u, v)

        if len(mst) == len(vertices) - 1:
            break

    return mst, total_weight

def test_kruskal():
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (3, 'B', 'C'),
        (2, 'B', 'D'),
        (5, 'C', 'E'),
        (2, 'D', 'E')
    ]

    mst1, total1 = kruskal_mst_basic(vertices, edges)
    mst2, total2 = kruskal_mst_optimized(vertices, edges)

    print("MST basic:")
    for u, v, w in mst1:
        print(f"{u}-{v} (w={w})")
    print("Tổng trọng số:", total1)

    print("\nMST optimized:")
    for u, v, w in mst2:
        print(f"{u}-{v} (w={w})")
    print("Tổng trọng số:", total2)

if __name__ == "__main__":
    test_kruskal()