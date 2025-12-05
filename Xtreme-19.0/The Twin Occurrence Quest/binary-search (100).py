import sys
from bisect import bisect_left, bisect_right

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

def solve_case():
    n = get_number()
    q = get_number()
    arr = [get_number() for _ in range(n)]
    
    for _ in range(q):
        target = get_number()
        
        l = bisect_left(arr, target)
        r = bisect_right(arr, target)

        if l == r:
            print(-1, -1)
        else:
            print(l + 1, r)


def main():
    solve_case()


if __name__ == "__main__":
    main()
