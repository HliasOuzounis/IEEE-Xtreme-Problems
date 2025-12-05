import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def dfs_depths(node, parent, depth, graph, depths, parents):
    depths[node] = depth
    parents[node] = parent
    
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs_depths(neighbor, node, depth + 1, graph, depths, parents)

def dfs_whites(node, parent, curr_dist, graph, whites, dist_to_white,):
    if whites[node] == 1:
        dist_to_white[node] = 0
    
    if curr_dist >= dist_to_white[node]:
        return
    
    dist_to_white[node] = curr_dist
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs_whites(neighbor, node, curr_dist + 1, graph, whites, dist_to_white)

def answer_query(u, v, depths, parents, dist_to_white):
    min_dist = min(dist_to_white[u], dist_to_white[v])
    if depths[u] > depths[v]:
        u, v = v, u
    
    while depths[v] > depths[u]:
        v = parents[v]
        min_dist = min(min_dist, dist_to_white[v])
    
    while u != v:
        u = parents[u]
        v = parents[v]
        min_dist = min(min_dist, dist_to_white[u], dist_to_white[v])
    
    min_dist = min(min_dist, dist_to_white[u])
    return min_dist


def main():
    n, q = get_numbers()
    whites = [0] + get_numbers()
    
    graph = defaultdict(set)
    for _ in range(n - 1):
        u, v = get_numbers()
        graph[u].add(v)
        graph[v].add(u)
        
    depths = [0] * (n + 1)
    parents = [0] * (n + 1)
    dist_to_white = [float('inf')] * (n + 1)
    dfs_depths(1, -1, 0, graph, depths, parents)
    
    for node in range(1, n + 1):
        if whites[node] == 1:
            dfs_whites(node, -1, 0, graph, whites, dist_to_white)
    
    for _ in range(q):
        u, v = get_numbers()
        print(answer_query(u, v, depths, parents, dist_to_white))
    


if __name__ == "__main__":
    main()