# Booking Concert Tickets in Groups
# Problem: https://leetcode.com/problems/booking-concert-tickets-in-groups/

from typing import List

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        # Segment Tree to store:
        # 1. max_val: maximum seats available in a single row in range
        # 2. sum_val: total seats available in range
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.max_tree = [0] * (2 * self.size)
        self.sum_tree = [0] * (2 * self.size)
        
        # Initialize
        # All rows have m seats initially
        self.build(1, 0, self.n - 1, m)
        
        # To track occupied seats per row (for gather)
        # Or just seats available
        self.row_seats = [m] * n
        # For scatter, we need to know where to start filling
        self.first_row_idx = 0

    def build(self, node, start, end, val):
        if start == end:
            self.max_tree[node] = val
            self.sum_tree[node] = val
            return
        mid = (start + end) // 2
        self.build(2*node, start, mid, val)
        self.build(2*node+1, mid + 1, end, val)
        self.max_tree[node] = max(self.max_tree[2*node], self.max_tree[2*node+1])
        self.sum_tree[node] = self.sum_tree[2*node] + self.sum_tree[2*node+1]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.max_tree[node] = val
            self.sum_tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2*node, start, mid, idx, val)
        else:
            self.update(2*node+1, mid + 1, end, idx, val)
        self.max_tree[node] = max(self.max_tree[2*node], self.max_tree[2*node+1])
        self.sum_tree[node] = self.sum_tree[2*node] + self.sum_tree[2*node+1]

    def query_max(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.max_tree[node]
        mid = (start + end) // 2
        return max(self.query_max(2*node, start, mid, l, r),
                   self.query_max(2*node+1, mid + 1, end, l, r))

    def query_sum(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.sum_tree[node]
        mid = (start + end) // 2
        return self.query_sum(2*node, start, mid, l, r) + \
               self.query_sum(2*node+1, mid + 1, end, l, r)

    # Find the smallest row index >= 0 such that row has >= k seats
    # Actually we only care about rows <= maxRow
    def find_first_row_k(self, node, start, end, max_r, k):
        if self.max_tree[node] < k or start > max_r:
            return -1
        if start == end:
            return start
        mid = (start + end) // 2
        # Try left child
        res = -1
        if self.max_tree[2*node] >= k:
            res = self.find_first_row_k(2*node, start, mid, max_r, k)
        
        if res != -1:
            return res
        
        return self.find_first_row_k(2*node+1, mid + 1, end, max_r, k)

    def gather(self, k: int, maxRow: int) -> List[int]:
        # Check if any row in [0, maxRow] has >= k seats
        # We need the smallest such row index
        r_idx = self.find_first_row_k(1, 0, self.n - 1, maxRow, k)
        if r_idx != -1:
            # We can book here
            # Starting seat?
            booked = self.m - self.row_seats[r_idx]
            self.row_seats[r_idx] -= k
            self.update(1, 0, self.n - 1, r_idx, self.row_seats[r_idx])
            return [r_idx, booked]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        # Check total capacity in [0, maxRow]
        total = self.query_sum(1, 0, self.n - 1, 0, maxRow)
        if total < k:
            return False
            
        # Perform booking
        # Greedily fill from lowest row
        # Optimization: start from first_row_idx which has seats?
        # Maybe slightly hard to track strictly but iterating is fine if amortized?
        # Since we deplete rows, we won't revisit them.
        
        # Find first row with available seats in range [0, maxRow]
        # Actually efficiently iterating: 
        # We can just iterate linearly from a cached 'start_ptr' because we completely fill rows.
        
        while k > 0 and self.first_row_idx <= maxRow:
            avail = self.row_seats[self.first_row_idx]
            if avail == 0:
                self.first_row_idx += 1
                continue
                
            take = min(k, avail)
            self.row_seats[self.first_row_idx] -= take
            self.update(1, 0, self.n - 1, self.first_row_idx, self.row_seats[self.first_row_idx])
            k -= take
            if self.row_seats[self.first_row_idx] == 0:
                self.first_row_idx += 1
                
        return True

if __name__ == "__main__":
    obj = BookMyShow(2, 5)
    print(obj.gather(4, 0)) # [0, 0]
    print(obj.gather(2, 0)) # []
    print(obj.scatter(5, 1)) # True
