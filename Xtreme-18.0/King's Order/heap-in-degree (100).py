import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    from collections import defaultdict
    from heapq import heappop, heappush
    n, m = get_numbers()
    
    group_id = [0] + get_numbers()
    in_degree = [0] * (n + 1)

    node_degrees = defaultdict(list)
    graph = defaultdict(list)
    for _ in range(m):
        a, b = get_numbers()
        in_degree[b] += 1
        graph[a].append(b)
    
    for i in range(1, n + 1):
        heappush(node_degrees[in_degree[i]], (group_id[i], i))
    
    result = []
    while node_degrees[0]:
        g_id, node = heappop(node_degrees[0])
        result.append(node)
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            heappush(node_degrees[in_degree[neighbour]], (group_id[neighbour], neighbour))
    
    if len(result) == n:
        print(*result)
    else:
        print(-1)
        

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
