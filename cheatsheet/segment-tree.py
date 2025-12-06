# ---------------- Segment Trees ---------------- #

# ---------------- 4n implementation ---------------- #

n = ...
segment_tree = [0] * 4 * n

# ---------------- Single Updates - Range Query ---------------- #

def update(node, l, r, idx, value):
    """
    Update the value at index idx to value in the segment tree
    """
    if l == r:
        segment_tree[node] = value
    else:
        mid = (l + r) // 2
        if idx <= mid:
            update(2 * node + 1, l, mid, idx, value)
        else:
            update(2 * node + 2, mid + 1, r, idx, value)

        # Update the parent node (sum/min/max/gcd/...)
        segment_tree[node] = segment_tree[2 * node + 1] + segment_tree[2 * node + 2]

def query(node, l, r, ql, qr):
    """
    Query the segment tree for the range [ql, qr]
    """
    if ql > r or qr < l:  # No overlap
        return 0  # or appropriate identity value for the operation
    
    if ql == l and qr == r: # perfect overlap
        return segment_tree[node]
    
    # Partial overlap
    mid = (l + r) // 2
    left_query = query(2 * node + 1, l, mid, ql, qr)
    right_query = query(2 * node + 2, mid + 1, r, ql, qr)

    # Combine results from left and right children
    # (sum/min/max/gcd/...)
    return left_query + right_query


# ---------------- Range Updates (lazy) ---------------- #

lazy_propagation = [0] * 4 * n 
# If lazy values can be 0 or negative, create a new array
marked = [False] * 4 * n

def push_lazy(node):
    if lazy_propagation[node] or marked[node]:
        # Apply the lazy value to the current node
        segment_tree[node] = lazy_propagation[node]
        
        # If not a leaf node, propagate the lazy value to children
        if node * 2 + 1 < len(segment_tree):
            lazy_propagation[node * 2 + 1] = lazy_propagation[node]
            lazy_propagation[node * 2 + 2] = lazy_propagation[node]
            marked[node * 2 + 1] = True
            marked[node * 2 + 2] = True
        
        # Clear the lazy value for the current node
        lazy_propagation[node] = 0
        marked[node] = False

def update_range(node, l, r, ql, qr, value):
    if ql > r or qr < l: # No overlap
        return
    
    if ql == l and qr == r: # Perfect overlap
        segment_tree[node] = value # Ex. assign value to range
        lazy_propagation[node] = value
        
        if segment_tree[node] < value: # Ex. Maximun in range
            segment_tree[node] = value
            lazy_propagation[node] = value    
        return
    
    push_lazy(node)
    mid = (l + r) // 2
    update_range(2 * node + 1, l, mid, ql, qr, value)
    update_range(2 * node + 2, mid + 1, r, ql, qr, value)

def query_range(node, l, r, ql, qr):
    if ql > r or qr < l:  # No overlap
        return 0  # or appropriate identity value for the operation
    
    push_lazy(node)  # Ensure current node is updated before querying
    
    if ql == l and qr == r:  # Perfect overlap
        return segment_tree[node]
    
    # Partial overlap
    mid = (l + r) // 2
    left_query = query_range(2 * node + 1, l, mid, ql, qr)
    right_query = query_range(2 * node + 2, mid + 1, r, ql, qr)

    # Combine results from left and right children
    return left_query + right_query
    
        
# ---------------- 2N implementation ---------------- #

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.seg = [0] * (2 * self.n)   # 2N memory

        # build leaves at indices [n .. 2n)
        for i in range(self.n):
            self.seg[self.n + i] = data[i]
        # build internal nodes [1 .. n-1]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.join(self.seg[i << 1], self.seg[i << 1 | 1])
    
    def join(self, left, right):
        return left + right

    def update(self, idx, value):
        """Point update: set a[idx] = value."""
        i = idx + self.n
        self.seg[i] = value
        i >>= 1
        while i:
            self.seg[i] = self.join(self.seg[i << 1], self.seg[i << 1 | 1])
            i >>= 1

    def query(self, left, right):
        """
        Range query on [left, right) (half-open).
        Returns sum of data[left:right].
        """
        res = 0 # Replace with identity element for other operations
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