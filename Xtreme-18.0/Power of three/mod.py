import sys
sys.set_int_max_str_digits(10**7)

input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_in_range(a, b):
    for i in range(a, b+1):
        if is_prime(i):
            return i


def solve_case():
    from math import log
    n = get_word()
    

    length = len(n)
    n = int(n)
    
    if n == 1:
        print(0)
        return
    
    log3_10 = log(10, 3)

    prime = prime_in_range(int(length * log3_10), int(length * log3_10) + 10)
    
    for x in range(1, prime):
        if 3**x % prime == n % prime:
            break
    else:
        print(-1)
        return
    
    primes = [10 ** 9 + 7, 998244353]
    n_mod_p = [n % p for p in primes]
    
    for p, n_mod in zip(primes, n_mod_p):
        if 3 ** x % p != n_mod:
            print(-1)
            return

    print(x)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
