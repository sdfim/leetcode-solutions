# Find Products of Elements of Big Array
# Problem: https://leetcode.com/problems/find-products-of-elements-of-big-array/

from typing import List

class Solution:
    def findProducts(self, queries: List[List[int]]) -> List[int]:
        res = []
        for a, b, mod in queries:
            res.append(self.solve_query(a, b, mod))
        return res

    def solve_query(self, start, end, mod):
        # We need sum of exponents for elements in range [start, end] (0-indexed)
        # 1-indexed range: [start+1, end+1]
        
        # Helper: Total set bits in 1..x
        def total_set_bits(x):
            count = 0
            bit = 0
            while (1 << bit) <= x:
                period = 1 << (bit + 1)
                half = 1 << bit
                full_cycles = (x + 1) // period
                count += full_cycles * half
                remainder = (x + 1) % period
                if remainder > half:
                    count += remainder - half
                bit += 1
            return count

        # Helper: Find number num such that 1..num contains at least k set bits
        def find_num(k):
            l, r = 1, 10**15
            ans = 1
            while l <= r:
                mid = (l + r) // 2
                if total_set_bits(mid) >= k:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

        # Total sum of exponents for all set bits in 1..x
        def total_exponent_sum(x):
            total_sum = 0
            bit = 0
            while (1 << bit) <= x:
                period = 1 << (bit + 1)
                half = 1 << bit
                
                # Count how many numbers in 1..x have this bit set
                full_cycles = (x + 1) // period
                count = full_cycles * half
                remainder = (x + 1) % period
                if remainder > half:
                    count += remainder - half
                
                total_sum += count * bit
                bit += 1
            return total_sum

        # Calculate exponent sum for range [1, limit] in the Big Array
        # The limit is index in Big Array (1-based count of elements)
        def calc_prefix_exponent_sum(limit):
            num = find_num(limit)
            # Full contribution from 1..(num-1)
            bits_before = total_set_bits(num - 1)
            sum_before = total_exponent_sum(num - 1)
            
            # Remaining elements to take from `num`
            needed = limit - bits_before
            
            # Extract set bits from `num` and take first `needed`
            current_sum = 0
            taken = 0
            # Iterate bits of num from LSB
            for i in range(60):
                if (num >> i) & 1:
                    current_sum += i
                    taken += 1
                    if taken == needed:
                        break
            
            return sum_before + current_sum

        # Range sum (start, end are 0-based indices)
        # Elements from start+1 to end+1 (1-based)
        sum_exponents = calc_prefix_exponent_sum(end + 1) - calc_prefix_exponent_sum(start)
        
        return pow(2, sum_exponents, mod)

if __name__ == "__main__":
    solution = Solution()
    print(solution.findProducts([[1, 3, 7]])) # Example
