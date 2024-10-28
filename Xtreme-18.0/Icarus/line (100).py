import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    moves = get_word()
    
    left = moves.count('L')
    right = moves.count('R')
    up = moves.count('U')
    
    n = len(moves)
    start = n
    end = 1
    
    if up > left:
        start, end = end, start
        
    print(n, start, end)

    for i in range(1, n):
        print(i + 1, 0) 
    print(0, 0)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
