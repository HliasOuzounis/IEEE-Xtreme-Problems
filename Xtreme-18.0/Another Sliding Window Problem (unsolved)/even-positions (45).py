# RUn with Pypy3
import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    n, q = get_numbers()
    
    a = get_numbers()
    
    for _ in range(q):
        x = get_number()
        
        ans = 0
        for mid_point in range(1, n):
            left = mid_point - 1
            right = mid_point
            max_sum = a[left] + a[right]
            
            while left >= 0 and right < n and max_sum <= x:
                if right < n - 1 and a[right + 1] <= x:
                    ans += a[right + 1] - a[left]
                    
                ans += a[right] - a[left]

                left -= 1
                right += 1
                if right < n:
                    max_sum = max(max_sum, a[left] + a[right])
                    
        print(ans)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
