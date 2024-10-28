import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n = get_number()
    
    temps = [get_numbers() for _ in range(n)]
    
    for temp1 in range(-100, 101):
        for temp2 in range(temp1, 101):
            stored = [False] * n
            for i, (ai, bi) in enumerate(temps):
                if ai <= temp1 <= bi or ai <= temp2 <= bi:
                    stored[i] = True
            
            if all(stored):
                print(temp1, temp2)
                return
    print(-1)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
