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
    
    if k <= 2 * l:
        first_bottom_left = (-l, -l)
        last_top_right = ((n - 1) * k + l, (n - 1) * k + l)
        big_square = (first_bottom_left[0] - last_top_right[0]) * (first_bottom_left[1] - last_top_right[1])
        
        first_top_left = (l, -l)
        last_top_left = ((n - 1) * k + l, (n - 1) * k - l)
        
        medium_square = (first_top_left[0] - last_top_left[0]) * (first_top_left[1] - last_top_left[1])

        small_square = k * k
        
        total_area = big_square - medium_square - small_square * (n - 1)
    
    else:
        total_area = 4 * l * l * n
        
    print(total_area)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
