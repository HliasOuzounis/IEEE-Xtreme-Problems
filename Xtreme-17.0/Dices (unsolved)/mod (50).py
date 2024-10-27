import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

def add_fractions(num1, denom1, num2, denom2):
    return (num1 * denom2 + num2 * denom1) % MOD, (denom1 * denom2) % MOD

def mod_inverse(num):
    return pow(num, MOD - 2, MOD)

from functools import lru_cache
sys.setrecursionlimit(10**6)
@lru_cache(maxsize=10**6)
def find_solutions(dice, tartget):
    if tartget <= 0:
        return 0, 1

    if dice * 6 < tartget:
        return 0, 1

    if dice == 1:
        return 1, 6

    num = 0
    denom = 1
    for i in range(1, 7):
        n, d = find_solutions(dice - 1, tartget - i)
        num, denom = add_fractions(num, denom, n, d)
        
    denom = (denom * 6) % MOD
    
    return num, denom
    
MOD = 998244353
def solve_case():
    n, k = get_numbers()
    
    num = 0
    denom = 1

    for i in range(1, k + 1):
        n1, d1 = find_solutions(i, n)
        num, denom = add_fractions(num, denom, n1, d1)
    
    print(num * mod_inverse(denom * k) % MOD)

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
