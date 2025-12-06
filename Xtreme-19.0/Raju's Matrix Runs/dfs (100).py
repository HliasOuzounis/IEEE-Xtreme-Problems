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


def dfs(i, j, curr_run, prev_val, n, m, matrix, run_count):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if run_count[i][j] > curr_run or matrix[i][j] <= prev_val:
        return
    run_count[i][j] = curr_run
    # move in 4 directions
    dfs(i + 1, j, curr_run + 1, matrix[i][j], n, m, matrix, run_count)
    dfs(i - 1, j, curr_run + 1, matrix[i][j], n, m, matrix, run_count)
    dfs(i, j + 1, curr_run + 1, matrix[i][j], n, m, matrix, run_count)
    dfs(i, j - 1, curr_run + 1, matrix[i][j], n, m, matrix, run_count)

def solve_case():
    n, m = get_numbers(2)
    matrix = []
    for _ in range(n):
        row = get_numbers(m)
        matrix.append(row)

    run_count = [[-1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if run_count[i][j] == -1:
                dfs(i, j, 0, -float('inf'), n, m, matrix, run_count)
    max_run = 0
    for i in range(n):
        for j in range(m):
            if run_count[i][j] > max_run:
                max_run = run_count[i][j]
    print(max_run + 1)


def main():
    for test_case in range(1):
        solve_case()


if __name__ == "__main__":
    main()
