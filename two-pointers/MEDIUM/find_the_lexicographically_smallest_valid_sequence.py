# Find the Lexicographically Smallest Valid Sequence
# Problem: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
# Solution:

from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        # last[j] = the last index in word1 that can complete word2[j:]
        last = [-1] * (m + 1)
        last[m] = n
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        res = []
        i = 0
        j = 0
        skipped = False
        
        while i < n and j < m:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not skipped and (j == m - 1 or last[j+1] > i): 
                # Can skip (change) this char if we can finish the rest
                # Actually problem is "change ONE character" effectively skipping match check once
                # We greedy pick earliest indices. 
                # If we encounter mismatch and haven't skipped yet, we check if we CAN skip.
                # We can skip if the rest of word2 (word2[j+1:]) can be formed by word1[i+1:].
                # Actually checks if rest of word2 can be found after current i.
                # Since we want lexicographically smallest indices, we prefer matching if possible?
                # No, we prefer smallest INDICES. i is the current index.
                # We ALWAYS take i if it matches.
                # If it doesn't match, we take i ONLY if we haven't skipped and rest is possible.
                res.append(i)
                j += 1
                skipped = True
            i += 1
            
        if len(res) == m:
            return res
        return []

if __name__ == "__main__":
    solution = Solution()
    
    w1 = "vbcca"
    w2 = "abc"
    print(f"Valid seq '{w1}', '{w2}': {solution.validSequence(w1, w2)}")
