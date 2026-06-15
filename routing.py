import heapq

def build_graph(edges):
    graph = {}
    for u, v, cost in edges:
        graph.setdefault(u, []).append((v, cost))
        graph.setdefault(v, []).append((u, cost))
    return graph

def dijkstra(graph, source):
    dist = {v: float("inf") for v in graph}
    parent = {v: None for v in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, parent

def shortest_route(graph, source, target):
    dist, parent = dijkstra(graph, source)
    if dist[target] == float("inf"):
        return None, []

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[target], path

def make_set(vertices):
    parent = {v: v for v in vertices}
    size = {v: 1 for v in vertices}
    return parent, size

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, size, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

def kruskal_mst(vertices, edges):
    parent, size = make_set(vertices)
    mst = []
    total = 0

    for w, u, v in sorted(edges):
        if union(parent, size, u, v):
            mst.append((u, v, w))
            total += w

    return mst, total

def demo_routing_shortest_path():
    edges = [
        ("WH1", "HCM", 4), ("WH1", "DN", 7),
        ("HCM", "DN", 2), ("HCM", "HN", 10),
        ("DN", "HN", 5), ("DN", "WH2", 3),
        ("WH2", "HN", 4)
    ]
    graph = build_graph(edges)
    cost, route = shortest_route(graph, "WH1", "HN")
    print("Route:", " -> ".join(route))
    print("Chi phí:", cost)

def demo_mst_network():
    vertices = ["WH1", "HCM", "DN", "HN", "WH2"]
    edges = [
        (4, "WH1", "HCM"), (7, "WH1", "DN"),
        (2, "HCM", "DN"), (10, "HCM", "HN"),
        (5, "DN", "HN"), (3, "DN", "WH2"),
        (4, "WH2", "HN")
    ]
    mst, total = kruskal_mst(vertices, edges)
    print("Mạng kho tối thiểu:")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")
    print("Tổng chi phí:", total)
    print("Đây là bộ khung tối thiểu, các tuyến giao hàng chi tiết dùng Dijkstra trên mạng này.")

def demo_routing_shortest_path():
    edges = [
        ("WH1", "HCM", 4), ("WH1", "DN", 7),
        ("HCM", "DN", 2), ("HCM", "HN", 10),
        ("DN", "HN", 5), ("DN", "WH2", 3),
        ("WH2", "HN", 4)
    ]
    graph = build_graph(edges)
    cost, route = shortest_route(graph, "WH1", "HN")
    print("Route:", " -> ".join(route))
    print("Chi phí:", cost)

def demo_routing_shortest_path():
    edges = [
        ("WH1", "HCM", 4), ("WH1", "DN", 7),
        ("HCM", "DN", 2), ("HCM", "HN", 10),
        ("DN", "HN", 5), ("DN", "WH2", 3),
        ("WH2", "HN", 4)
    ]
    graph = build_graph(edges)
    cost, route = shortest_route(graph, "WH1", "HN")
    print("Route:", " -> ".join(route))
    print("Chi phí:", cost)
    
def demo_mst_network():
    vertices = ["WH1", "HCM", "DN", "HN", "WH2"]
    edges = [
        (4, "WH1", "HCM"), (7, "WH1", "DN"),
        (2, "HCM", "DN"), (10, "HCM", "HN"),
        (5, "DN", "HN"), (3, "DN", "WH2"),
        (4, "WH2", "HN")
    ]
    mst, total = kruskal_mst(vertices, edges)
    print("Mạng kho tối thiểu:")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")
    print("Tổng chi phí:", total)