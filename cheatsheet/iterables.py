# ---------------- Iterables ---------------- #


def lexicographically_smaller(a, b):
    """
    Check if iterable a is lexicographically smaller than b
    """
    for ai, bi in zip(a, b):
        if ai > bi:
            return False
        if ai < bi:
            return True

    return len(a) <= len(b)


# ---------------- Arrays ---------------- #

def kadanes_algorithm(array):
    """
    Find the maximum sum subarray O(n)
    """
    n = len(array)

    ans = array[0]
    ans_l = ans_r = 0
    sum_ = 0
    last_neg = -1
    
    for r in range(n):
        sum_ += array[r]
        
        if sum_ > ans:
            ans = sum_
            ans_l = last_neg + 1
            ans_r = r
        
        if sum_ < 0:
            sum_ = 0
            last_neg = r

    return ans, ans_l, ans_r

# ---------------- Matrices ---------------- #

def maximum_sum_submatrix(matrix):
    """
    Return the maximum sum submatrix O(n^3)
    """
    
    n, m = len(matrix), len(matrix[0])
    
    ans = float('-inf')
    
    ans_r1 = ans_r2 = ans_c1 = ans_c2 = 0
    
    for l in range(m):
        row_sum = [0] * n
        for r in range(l, m):
            for i in range(n):
                row_sum[i] += matrix[i][r]

            sum_, row_l, row_r = kadanes_algorithm(row_sum)

            if sum_ > ans:
                ans = sum_
                ans_r1, ans_r2, ans_c1, ans_c2 = row_l, row_r, l, r 

    return ans, ans_r1, ans_r2, ans_c1, ans_c2


def sparse_matrix_fill(matrix):
    """
    Sparse range updates for a matrix O(1)
    And the calculation of the final values O(n*m)
    """
    n, m = len(matrix), len(matrix[0])
    
    ranges = [...]
    
    for (r1, c1, r2, c2, val) in ranges:
        matrix[r1][c1] += val
        matrix[r1][c2 + 1] -= val
        matrix[r2 + 1][c1] -= val
        matrix[r2 + 1][c2 + 1] += val
    
    for i in range(m):
        matrix[0][i] += matrix[0][i - 1]
    
    for i in range(n):
        matrix[i][0] += matrix[i - 1][0]
        for j in range(1, m):
            matrix[j][i] += matrix[j - 1][i] + matrix[j][i - 1] - matrix[j - 1][i - 1]
            
            
# ---------------- Strings ---------------- #

def string_hash(s):
    """
    Compute hashes for entire string prefixes [0, i] O(n)
    """
    hashes = [0] * len(s)
    p = 31
    p_pow = 1
    m = 10**9 + 9
    for i, c in enumerate(s):
        hashes[i] = (hashes[i - 1] + ord(c) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hashes

def substring_hash(hashes, l, r, p, m):
    """
    Compute hash for substring [l, r] O(1)
    """
    if l == 0:
        return hashes[r]
    return ((hashes[r] - hashes[l - 1]) * mod_inverse(p, l, m)) % m

def mod_inverse(base, exp, m):
    return pow(base, exp - 2, m)


def manacher(s):
    ss = '#' + '#'.join(s) + '#'

    RL = [0] * len(ss)
    max_right, mr_center = -1, -1

    for i in range(len(ss)):
        R = 1
        if i < max_right:
            mr_mirror = mr_center - (i - mr_center)
            R = min(RL[mr_mirror], max_right - i)

        while i - R >= 0 and i + R < len(ss) and ss[i - R] == ss[i + R]:
                R += 1

        RL[i] = R
        if max_right < i + R-1:
            max_right = i + R-1
            mr_center = i

    return RL
        
# ---------------- Tetsing ---------------- #

def test():
    s = "Hello World"
    
    h = string_hash(s)
    assert substring_hash(h, 1, -3, 31, 10**9 + 9) == string_hash(s[1:-2])[-1]
    
    
    
if __name__ == "__main__":
    test()