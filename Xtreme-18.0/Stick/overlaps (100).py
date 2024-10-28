import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n, k, l = get_numbers()
    
    square_area = 4 * l * l
    
    total_area = square_area

    if k >= 2 * l:
        extra_area = square_area
    else:
        extra_area = 4 * l * l - (2 * l - k) * (2 * l - k)
    
    
    total_area += extra_area * (n - 1)
    
    print(total_area)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
