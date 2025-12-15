# Split Message Based on Limit
# Problem: https://leetcode.com/problems/split-message-based-on-limit/

from typing import List

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        
        # Iterate through possible number of parts `k`.
        # `k` won't realistically exceed n.
        
        # Suffix is "<j>/<k>".
        # Length of suffix depends on len(str(j)) and len(str(k)).
        # Cost for part j (1-based): 3 + len(str(j)) + len(str(k))
        # Content capacity for part j: limit - cost
        
        # We can iterate k.
        # But wait, checking every k up to N is slow if N is large?
        # N=10^4. It's fine.
        
        # Optimization: We can jump ranges of k where len(str(k)) is constant.
        # len(str(k)): 1 (1-9), 2 (10-99), 3 (100-999), 4 (1000-9999).
        
        # Cumulative capacity for k parts needs to be >= n.
        
        cum_cap = 0
        k = 1
        
        while True:
            # We want to check if `k` parts are enough.
            # But calculating exact capacity for `k` parts involves summing capacities of 1..k.
            
            lk = len(str(k))
            if 3 + lk + 1 > limit: # Minimal suffix is <a>/<b> where a is 1 digit
                # Even the first part 1/<k> is too big?
                # Actually, 1/<k> takes 3 + 1 + lk space.
                pass
            
            # Since we increment k by 1, we can incrementally update capacity.
            # Capacity of new part `k` is: limit - (3 + len(str(k)) + len(str(k)))?
            # No, when we move from k-1 parts to k parts, ALL parts change suffix form /<k-1> to /<k>.
            # That changes the denominator length for all previous parts if len(str(k)) > len(str(k-1)).
            
            # Since checking is complex, let's just check ranges of k.
            pass
            if k > n: # Heuristic, if k > n, we are splitting into 1-char pieces or worse
                 break
        
        # Re-approach: Iterate k.
        # Calculate total capacity for k parts.
        # Total capacity = sum(limit - (3 + len(str(i)) + len(str(k)))) for i in 1..k
        # = k * limit - 3*k - k*len(str(k)) - sum(len(str(i)) for i in 1..k)
        
        # We can maintain sum_len_i.
        
        sum_len_i = 0
        k = 1
        while k <= n + 1000: # Slightly loose bound
            sl = len(str(k))
            if 3 + sl + sl > limit: 
                # Impossible if even the longest suffix doesn't fit?
                # Actually smallest suffix is 1/k.
                # If limit <= 3 + 1 + sl, part 1 can't hold any content?
                pass
            
            # Check if 1/k fits.
            if 3 + 1 + sl > limit:
                 # Even part 1 can't fit data. But we iterate upwards.
                 # If limit is small, we eventually fail or succeed?
                 pass

            sum_len_i += sl
            
            # Total capacity
            # capacity = k * (limit - 3 - sl) - sum_len_i
            capacity = k * (limit - 3 - sl) - sum_len_i
            
            if capacity >= n:
                # Construct result
                res = []
                cursor = 0
                for i in range(1, k + 1):
                    suffix = f"<{i}/{k}>"
                    rem_len = limit - len(suffix)
                    # consume rem_len chars from message at cursor
                    chunk = message[cursor : cursor + rem_len]
                    res.append(chunk + suffix)
                    cursor += rem_len
                return res
            
            k += 1
            
        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.splitMessage("this is really a very awesome message", 9))
    # Output: ["thi<1/14>", "s <2/14>", ...]
