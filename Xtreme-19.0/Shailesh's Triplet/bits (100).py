# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
def get_numbers(n):
    return [get_number() for _ in range(n)]


def find_smallest_differing_bit(a, b):
    xor = a ^ b
    if xor == 0:
        return -1
    return (xor & -xor).bit_length() - 1
    
def solve_case():
    # If n is odd, task impossible due to parity
    # Initial idea is A=n, B=C=n/2
    # Immediately A+B+C = 2n and A^B^C = n
    # Need to adjust A and B to make B != C
    n = get_number()
    
    if n % 2 == 1:
        print(-1)
        return
    
    A = n
    B = n // 2
    C = n // 2
    
    j = find_smallest_differing_bit(A, B)
    if (1 << j) == B:
        print(-1)
        return
    
    if B & (1 << j):
        B -= (1 << j)
        A += (1 << j)
    else:
        B += (1 << j)
        A -= (1 << j)
    
    print(A, B, C)

def main():
    for test_case in range(total_cases := get_number()):
        solve_case()
        
        
if __name__ == "__main__":
    main()