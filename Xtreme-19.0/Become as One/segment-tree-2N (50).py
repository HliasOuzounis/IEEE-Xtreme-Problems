# Using 2N implementation of segment tree
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

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.seg = [{} for _ in range(2 * self.n)]   # 2N memory

        # build leaves at indices [n .. 2n)
        for i in range(self.n):
            self.seg[self.n + i][data[i]] = 1
        # build internal nodes [1 .. n-1]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.join(self.seg[i << 1], self.seg[i << 1 | 1])

    def join(self, left, right):
        result = {}
        for key in left:
            result[key] = result.get(key, 0) + left[key]
        for key in right:
            result[key] = result.get(key, 0) + right[key]
        
        # for i in range(max_A + 1):
        #     if i not in result:
        #         continue
        #     if result[i] > 1:
        #         carry = result[i] // 2
        #         result[i] = result[i] % 2
        #         result[i + 1] = result.get(i + 1, 0) + carry
        
        return result

    def query(self, left, right):
        """
        Range query on [left, right) (half-open).
        """
        res = {}
        l = left + self.n
        r = right + self.n
        while l < r:
            if l & 1:
                res = self.join(res, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.join(res, self.seg[r])
            l >>= 1
            r >>= 1
        return res
    
def answer_query(result):
    s = sum(result.values())
    
    for i in range(max_A + 1):
        if i not in result:
            result[i] = 0
        if i + 1 not in result:
            result[i + 1] = 0
        
        if s == 1:
            return 'Yes'
        if result[i] % 2 == 1:
            return 'No'
        result[i + 1] += result[i] // 2
        s -= result[i] // 2
    
    while s > 1:
        if s % 2 == 1:
            return 'No'
        s //= 2
    return 'Yes'
        

def solve_case():
    n, q  = get_numbers(2)
    arr = get_numbers(n)
    
    seg_tree = SegmentTree(arr)
    
    for _ in range(q):
        ql, qr = get_numbers(2)
        result = seg_tree.query(ql - 1, qr)
        print(answer_query(result))
        
def main():
    for test_case in range(1):
        solve_case()


if __name__ == "__main__":
    main()