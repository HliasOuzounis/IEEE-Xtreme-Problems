import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()



def check(n, e, curr_idx, parity):
    if n == 0:
        return 0

    ans = n * (1 if parity else -1)

    if curr_idx == len(e):
        return ans

    for i in range(curr_idx, len(e)):
        ans += check(n // e[i], e, i + 1, not parity)

    return ans


def solve_case():
    n, k = get_numbers()
    e = get_numbers()

    e.sort()

    print(n - check(n, e, 0, True))


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()