# Pour Water Between Buckets to Make Water Equal
# Problem: https://leetcode.com/problems/pour-water-between-buckets-to-make-water-equal/

from typing import List

class Solution:
    def pourWater(self, buckets: List[int], loss: int) -> float:
        # loss is percentage. If we pour X, receiver gets X * (1 - loss/100).
        
        if not buckets: return 0.0
        
        # Binary search for target value 'v'.
        # Can we achieve 'v' in all buckets?
        
        def check(target):
            give = 0.0
            need = 0.0
            for b in buckets:
                if b > target:
                    give += (b - target)
                else:
                    need += (target - b)
                    
            # We can give `give`. After loss, this becomes `give * ratio`.
            # This reduced amount must satisfy `need`.
            
            ratio = 1.0 - loss / 100.0
            return give * ratio >= need
            
        low, high = 0.0, max(buckets) * 1.0 # Or sum? No max is enough upper bound for average.
        # Actually max possible is max(buckets)? No, sum/len not really bound if loss is 0.
        # Safe upper bound is max(buckets).
        
        # Run for fixed iterations for precision
        for _ in range(100):
            mid = (low + high) / 2
            if check(mid):
                low = mid
            else:
                high = mid
                
        return low

if __name__ == "__main__":
    solution = Solution()
    print(f"{solution.pourWater([3,5,7,7], 25):.5f}") 
