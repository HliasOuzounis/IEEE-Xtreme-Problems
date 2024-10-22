import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def mod_inverse(num):
    return pow(num, MOD - 2, MOD)

def add_fractions(num1, denom1, num2, denom2):
    return (num1 * denom2 + num2 * denom1) % MOD, (denom1 * denom2) % MOD

    
MOD = 998244353
def solve_case():
    n, k = get_numbers()
    
    dp = [1] * 7
    dp[0] = 0
        
    num = 1 if n <= 6 else 0
    denom = 6 if n <= 6 else 1
    
    for dice in range(2, k + 1):
        new_dp = [0] * (6 * dice + 1)
        for s in range(1, 6 * dice + 1):
            for face in range(1, 7):
                if s - face <= 0 or s - face >= len(dp):
                    continue
                new_dp[s] = (new_dp[s] + dp[s - face]) % MOD
        
        
        dp = new_dp
        if n < len(dp):
            num, denom = add_fractions(num, denom, dp[n], pow(6, dice, MOD))
    
    print(num * mod_inverse(denom * k) % MOD)
    
    
    

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
