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

# Something is wrong here
def dijkstra(graph, start_node):
    """
    Dijkstra's algorithm to find the shortest path from start_node to all other nodes
    Graph must be a dictionary with the following structure:
    graph = {node: [(neighbour, weight), ...]}
    """
    from heapq import heappush, heappop

    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    total_risks = {node: float("inf") for node in graph}
    total_risks[start_node] = 0
    visited = set()
    queue = [(0, 0, start_node)]

    while queue:
        risk, dist, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)

        for neighbour, weight, added_risk in graph[node]:
            if neighbour not in visited:
                new_dist = dist + weight
                new_risk = max(risk, added_risk)
                if new_risk < total_risks[neighbour] or (new_risk == total_risks[neighbour] and new_dist < distances[neighbour]):
                    distances[neighbour] = new_dist
                    total_risks[neighbour] = new_risk
                    heappush(queue, (new_risk, new_dist, neighbour))

    return distances, total_risks


def solve_case():
    n, m = get_numbers(2)
    graph = defaultdict(list)    
    for _ in range(m):
        u, v, w, r = get_numbers(4)
        graph[u].append((v, w, r))
        graph[v].append((u, w, r))
    
    graph[n] = []  # Ensure the destination node is in the graph
        
    distances, risks = dijkstra(graph, 1)
    if distances[n] == float("inf"):
        print(-1)
    else:
        print(risks[n], distances[n])


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
