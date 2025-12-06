# Same algo works in C++. Python gets memory errors on large inputs.
# Task should have 512MB limit instead of 256MB.

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


def answer_query(counts_arr, ql, qr, max_A):
    c = 0
    last_num = None
    for num in range(max_A + 1):
        count = counts_arr[qr][num] - counts_arr[ql - 1][num] + c
        if count % 2 == 1 and count > 1:
            return 'No'
        elif count == 1:
            if last_num is not None:
                return 'No'
            last_num = num
        c = count // 2
        
    return 'Yes'

def solve_case():
    max_A = 30
    n, q = get_numbers(2)
    
    counts_arr = [[0] * (max_A + 1) for _ in range(n + 1)]
    for i in range(n):
        val = get_number()
        counts_arr[i + 1][val] += 1

    for i in range(1, n + 1):
        for j in range(max_A + 1):
            counts_arr[i][j] += counts_arr[i - 1][j]

    for _ in range(q):
        ql, qr = get_numbers(2)
        print(answer_query(counts_arr, ql, qr, max_A))
            

def main():
    for test_case in range(1):
        solve_case()


if __name__ == "__main__":
    main()
