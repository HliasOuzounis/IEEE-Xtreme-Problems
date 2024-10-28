import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


from bisect import bisect_right
def solve_case():
    l, n, m = get_numbers()
    
    a = []
    b = []
    
    a_wall = 0
    res = 1
    for _ in range(n):
        wall, cord = get_word().split()
        if wall == "R":
            a_wall += 1
        else:
            a.append(int(cord))
            
        res += 1

    a.sort()
    
    b_wall = 0
    for _ in range(m):
        wall, cord = get_word().split()
        if wall == "L":
            b_wall += 1
        else:
            b.append(int(cord))
            
    res = (b_wall + 1) * res
    
    for bi in b:
        idx = bisect_right(a, bi)
        res += len(a) - idx + a_wall + 1
    
    print(res)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
