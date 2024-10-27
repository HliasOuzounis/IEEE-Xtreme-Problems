import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


p = 31
m = 10**9 + 9


def string_hash(s):
    hashes = [0] * len(s)
    p_pow = 1
    for i, c in enumerate(s):
        hashes[i] = (hashes[i - 1] + ord(c) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hashes


def mod_inverse(base, exp, m):
    return pow(base, exp - 2, m)


def substring_hash(hashes, l, r):
    if l == 0:
        return hashes[r]
    return ((hashes[r] - hashes[l - 1]) * mod_inverse(p, l, m)) % m


def check_pass(old, new, sequences):
    old = "ω" + old + "ω"
    new = "ω" + new + "ω"
    old_hash = string_hash(old)
    new_hash = string_hash(new)
    
    old_rev_hash = string_hash(old[::-1])
    new_rev_hash = string_hash(new[::-1])
        
    small_len = min(len(old), len(new))
    max_len = max(len(old), len(new))
    

    for start in range(small_len):
        if old_hash[start] != new_hash[start]:
            break
        for end in range(-1, -small_len - 1, -1):
            if start > small_len + end:
                break
            
            if old_rev_hash[-end - 1] != new_rev_hash[-end - 1]:
                break

            s_old = old[start + 1 : end]
            s_new = new[start + 1 : end]
            
            if not s_old or not s_new:
                continue
            
            if s_old not in sequences or s_new not in sequences:
                continue
            
            if sequences[s_old] == sequences[s_new]:
                print("REJECT")
                return

    print("OK")


def solve_case():
    n = get_number()

    from collections import defaultdict

    sequences = defaultdict(int)

    for i in range(n):
        seq_values = get_word().split(" ")[1:]
        for seq in seq_values:
            sequences[seq] = i

    passwords = get_number()
    for _ in range(passwords):
        old, new = get_word().split(" ")

        check_pass(old, new, sequences)


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
