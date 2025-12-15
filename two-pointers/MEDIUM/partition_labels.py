# Partition Labels
# Problem: https://leetcode.com/problems/partition-labels/
# Solution:

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "ababcbacadefegdehijhklij"
    print(f"Partition labels for '{s1}': {solution.partitionLabels(s1)}")
    
    s2 = "eccbbbbdec"
    print(f"Partition labels for '{s2}': {solution.partitionLabels(s2)}")
