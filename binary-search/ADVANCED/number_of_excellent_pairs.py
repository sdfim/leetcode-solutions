# Number of Excellent Pairs
# Problem: https://leetcode.com/problems/number-of-excellent-pairs/
# (LC 2354)

from typing import List

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Condition: bits(x | y) + bits(x & y) >= k
        # Identity: bits(x | y) + bits(x & y) = bits(x) + bits(y)
        # So we need bits(x) + bits(y) >= k.
        # Only distinct numbers matter.
        
        unique_nums = list(set(nums))
        bit_counts = []
        for x in unique_nums:
            bit_counts.append(bin(x).count('1'))
            
        bit_counts.sort()
        n = len(bit_counts)
        ans = 0
        
        # Two pointers
        l, r = 0, n - 1
        while l <= r:
            if bit_counts[l] + bit_counts[r] >= k:
                # If l and r work, then (l, r), (l, r-1)... (l, l) work?
                # No, if l+r >= k, then r matched with anything >= l works.
                # Since array is sorted.
                # For fixed l, we need index j such that bits[j] >= k - bits[l].
                # Since r works, all indices from r down to l work?
                # Yes, bits[r] >= bits[r-1] >= ...
                # Wait, we need to count pairs (nums[i], nums[j]).
                # Are (l, r) and (r, l) distinct? Yes, "pairs".
                # If we pick two DIFFERENT indices i, j: contributes 2.
                # If i == j: contributes 1.
                
                # Logic:
                # For current l, valid r's are in [limit, n-1].
                # We can just count valid pairs using integration.
                # Actually, simpler:
                # Iterate l from 0 to n-1. Find smallest r >= l such that bits[l] + bits[r] >= k.
                pass
                
                # Standard Two Pointers for count >= K in sorted array:
                # l moves forward. r moves backward.
                # count pairs (i, j) i <= j.
                # If bits[l] + bits[r] >= k:
                # Then for this r, all l' in [l, r] work? No.
                # If bits[l] + bits[r] >= k. Since bits increasing.
                # Then bits[r] + bits[anything >= l] >= k.
                # So r pairs with (r - l + 1) elements?
                # Contributions: (r, l), (r, l+1) ... (r, r).
                # Each distinct pair counts 2, self counts 1.
                # Just add 2 * (r - l) + 1 ?
                # ans += 2 * (r - l) + 1
                # r -= 1
            else:
                l += 1
                
        # Correct logic:
        # l, r.
        # If bits[l] + bits[r] < k: l++ (need more bits).
        # If bits[l] + bits[r] >= k:
        #   All indices j in [l, r] satisfy bits[j] + bits[r] >= k.
        #   So r forms pairs with r, r-1, ..., l.
        #   Total pairs involving r: (r - l + 1) * 2 - (1 if equal)?
        #   Usually easier: count valid (i, j) with i < j, multiply by 2, add i==j count.
        pass
    
        # Re-impl two pointers properly:
        ans = 0
        l, r = 0, n - 1
        while l <= r:
            if bit_counts[l] + bit_counts[r] >= k:
                # indices r can pair with l, l+1, ... r.
                # Number of such indices is (r - l + 1).
                # We count for 'l' specifically?
                # If we fix `l`, valid `j` are `r, r-1 ...`.
                # If we fix `r`, valid `i` are `l, l+1 ... r` (since bits[l] is smallest valid).
                # Number of elements >= bits[l] is matching with r.
                # So r contributes (r - l + 1) * 2 - 1 ?
                # (since (r,r) counts once, (r, x) counts twice).
                ans += (r - l) * 2 + 1
                # Move r left (to separate it)
                r -= 1
            else:
                l += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.countExcellentPairs([1,2,3,1], 3)) # 5
