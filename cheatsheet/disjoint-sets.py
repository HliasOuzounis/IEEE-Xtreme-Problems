# ---------------- Disjoint Set Union ---------------- #

# root = [i for i in range(n)]   The root of the set each node belongs to
# size = [1] * n                 The size of each set

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

# ---------------- Kruskal's Algorithm ---------------- #

def kruskal(n, edges):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph
    edges should be a list of tuples (weight, u, v)
    """
    # Sort edges by weight
    edges.sort()
    
    root = [i for i in range(n)]
    size = [1] * n
    
    mst_weight = 0
    mst_edges = []
    
    for weight, u, v in edges:
        if find_root(root, u) != find_root(root, v):
            union_sets(root, size, u, v)
            mst_weight += weight
            mst_edges.append((u, v, weight))
    
    return mst_weight, mst_edges