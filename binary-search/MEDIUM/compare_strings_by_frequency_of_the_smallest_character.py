# Compare Strings by Frequency of the Smallest Character
# Problem: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            if not s: return 0
            smallest_char = min(s)
            return s.count(smallest_char)
            
        words_freq = sorted([f(w) for w in words])
        res = []
        n = len(words_freq)
        
        for q in queries:
            freq = f(q)
            # Find count of words with frequency > freq
            # bisect_right returns index after largest <= freq, so valid range is [idx, n)
            idx = bisect.bisect_right(words_freq, freq)
            res.append(n - idx)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSmallerByFrequency(["cbd"], ["zaaaz"]))  # Output: [1]
