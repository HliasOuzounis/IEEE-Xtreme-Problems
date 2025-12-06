# Run with Python3
from collections import defaultdict

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
def get_numbers(n):
    return [get_number() for _ in range(n)]

def find_root(root, node):
    """
    Find the root of a node in a disjoint set
    """
    if root[node] != node:
        root[node] = find_root(root, root[node])
    return root[node]

def union_sets(root, size, a, b):
    """
    Union sets that contain a and b
    (root a is the root of the new joint set)
    """
    a = find_root(root, a)
    b = find_root(root, b)

    if a == b:
        return
    
    if size[a] < size[b]:
        a, b = b, a
    
    size[a] += size[b]
    root[b] = a
    
def kruskal(n, edges):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph
    edges should be a list of tuples (weight, u, v)
    """
    # Sort edges by weight (risk)
    edges.sort()
    
    root = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    
    mst_risks = 0
    mst_edges = []
    
    for risk, time, u, v in edges:
        if find_root(root, u) != find_root(root, v):
            union_sets(root, size, u, v)
            mst_risks = max(mst_risks, risk)
            mst_edges.append((u, v, time))
        # Stop condition. Find max risk needed to connect 1 and n
        if find_root(root, 1) == find_root(root, n):
            return mst_risks
        
    if find_root(root, 1) != find_root(root, n):
        return float("inf")


def dijkstra(graph, start_node):
    """
    Dijkstra's algorithm to find the shortest path from start_node to all other nodes
    Graph must be a dictionary with the following structure:
    graph = {node: [(neighbour, weight), ...]}
    """
    from heapq import heappush, heappop

    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    visited = set()
    queue = [(0, start_node)]

    while queue:
        dist, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_dist = dist + weight
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    heappush(queue, (new_dist, neighbour))

    return distances

def solve_case():
    n, m = get_numbers(2)
    
    edges = []
    for _ in range(m):
        u, v, w, r = get_numbers(4)
        edges.append((r, w, u, v))
    
    risk = kruskal(n, edges)
    if risk == float("inf"):
        print(-1)
        return
    
    graph = defaultdict(list)
    graph[n] = [] # Ensure the destination node is in the graph
    for r, w, u, v in edges:
        if r > risk:
            continue
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    distances = dijkstra(graph, 1)
    if distances[n] == float("inf"):
        print(-1)
    else:
        print(risk, distances[n])


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
