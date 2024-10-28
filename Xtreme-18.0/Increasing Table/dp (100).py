import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

MOD = 998244353

def search(top, bottom, num, a, b, n, c):
    if num == 0 and top == n and bottom == n:
        return 1
    
    if c[num][bottom - top] != -1:
        return c[num][bottom - top]
        
    if (
        top > n or bottom > n or top > bottom or
        num in a and num in b or
        num in a and top == n or
        num in b and bottom == n
    ):
        return 0

    if num in a:
        ways = search(top + 1, bottom, num - 1, a, b, n, c)
    elif num in b:
        ways = search(top, bottom + 1, num - 1, a, b, n, c)
    else:
        ways = (search(top + 1, bottom, num - 1, a, b, n, c) + search(top, bottom + 1, num - 1, a, b, n, c))

    c[num][bottom - top] = ways % MOD
    
    return c[num][bottom - top]


def solve_case():
    n = get_number()
    
    a = set(get_numbers()[1:])
    b = set(get_numbers()[1:])
    
    c = [[-1] * 4001 for _ in range(4001)]
    
    print(search(0, 0, 2 * n, a, b, n, c))


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
