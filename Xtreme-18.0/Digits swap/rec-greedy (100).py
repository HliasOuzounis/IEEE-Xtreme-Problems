import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def decide_swap(n, k, i):
    if k == 0 or i == len(str(n)) - 1:
        return n
    
    best_n = n
        
    max_digit = -float("inf")
    max_index = [i]
    
    for j in range(i, len(n)):
        num = n[j]
        if int(num) > max_digit:
            max_digit = int(num)
            max_index = [j]
        elif int(num) == max_digit:
            max_index.append(j)
            
    not_swapped = i in max_index
    if not_swapped:
        return max(best_n, decide_swap(n, k, i + 1))
        
    for index in max_index: 
        if index == i:
            continue
        
        new_n = list(n)
        new_n[i], new_n[index] = new_n[index], new_n[i]
        new_n = tuple(new_n)
        
        best_n = max(best_n, decide_swap(new_n, k - 1, i + 1))

    return best_n


def solve_case():
    n, k = get_numbers()
    
    n = tuple(str(n))
    
    print("".join(decide_swap(n, k, 0)))


def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
