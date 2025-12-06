max_A = 30

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


def update(node, l, r, idx, value, segment_tree):
    """
    Update the value at index idx to value in the segment tree
    """
    if l == r:
        segment_tree[node][value] = 1
    else:
        mid = (l + r) // 2
        if idx <= mid:
            update(2 * node + 1, l, mid, idx, value, segment_tree)
        else:
            update(2 * node + 2, mid + 1, r, idx, value, segment_tree)

        # Update the parent node (sum/min/max/gcd/...)
        # segment_tree[node] = segment_tree[2 * node + 1] + segment_tree[2 * node + 2]
        for i in range(max_A + 1):
            segment_tree[node][i] = segment_tree[2 * node + 1][i] + segment_tree[2 * node + 2][i]

def query(node, l, r, ql, qr, segment_tree):
    """
    Query the segment tree for the range [ql, qr]
    """
    if ql > r or qr < l:  # No overlap
        return [0] * (max_A + 1)  # or appropriate identity value for the operation
    
    if ql <= l and qr >= r: # perfect overlap
        return segment_tree[node]
    
    # Partial overlap
    mid = (l + r) // 2
    left_query = query(2 * node + 1, l, mid, ql, qr, segment_tree)
    right_query = query(2 * node + 2, mid + 1, r, ql, qr, segment_tree)

    # Combine results from left and right children
    # (sum/min/max/gcd/...)
    for i in range(max_A + 1):
        left_query[i] += right_query[i]
    return left_query


def solve_case():
    n, q  = get_numbers(2)
    arr = get_numbers(n)
    
    segment_tree = [[0 for _ in range(max_A + 1)] for _ in range(4 * n)]
    
    for i in range(n):
        update(0, 0, n - 1, i, arr[i], segment_tree)

    # print(segment_tree)
    for _ in range(q):
        ql, qr = get_numbers(2)
        result = query(0, 0, n - 1, ql - 1, qr - 1, segment_tree) + [0]
        s = sum(result)
        
        flag = False
        for i in range(max_A + 1):
            if s == 1:
                print('Yes')
                flag = True
                break
            if result[i] % 2 == 1:
                print('No')
                flag = True
                break
            result[i+1] += result[i] // 2
            s -= result[i] // 2
        if flag:
            continue
        
        while s > 1:
            if s % 2 == 1:
                print('No')
                break
            s //= 2
        else:
            if s == 1:
                print('Yes')

def main():
    for test_case in range(1):
        solve_case()

if __name__ == "__main__":
    main()