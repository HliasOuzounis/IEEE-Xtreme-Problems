import sys


input = lambda: sys.stdin.readline().rstrip()

MOD = 10**9 + 7

def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case(dp):
    n, m, a = get_numbers()
    
    target = n * 53 * 100 # In piasters
    target //= 25  # In 25-piaster units
    
    ans = dp[target]
    if m == a == ans:
        return 'TIE'
        
    if abs(m - ans) < abs(a - ans):
        return 'Mikel'
    elif abs(m - ans) > abs(a - ans):
        return 'Andrew'
    else:
        return 'NONE'
    

def main():
    max_val = 10 ** 5 * 53 * 100
    dp = [0] * (max_val // 25 + 2)
    
    coins = [0.25, 0.5, 1, 5, 10, 20, 50, 100, 200]
    for i, c in enumerate(coins):
        coins[i] = int(c * 100) // 25  # In 25-piaster units
        
    dp[0] = 1
    
    for i in range(1, max_val // 25 + 2):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = (dp[i] + dp[i - coin]) % MOD

    for test_case in range(total_cases := get_number()):
        print(solve_case(dp))


if __name__ == "__main__":
    main()
