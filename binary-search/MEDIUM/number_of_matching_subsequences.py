# Number of Matching Subsequences
# Problem: https://leetcode.com/problems/number-of-matching-subsequences/

from typing import List
import collections
import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = collections.defaultdict(list)
        for i, char in enumerate(s):
            indices[char].append(i)
            
        count = 0
        for word in words:
            curr = -1
            found = True
            for char in word:
                idx_list = indices[char]
                idx = bisect.bisect_right(idx_list, curr)
                if idx < len(idx_list):
                    curr = idx_list[idx]
                else:
                    found = False
                    break
            if found:
                count += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.numMatchingSubseq("abcde", ["a","bb","acd","ace"]))  # Output: 3
