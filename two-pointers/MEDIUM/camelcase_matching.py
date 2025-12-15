# Camelcase Matching
# Problem: https://leetcode.com/problems/camelcase-matching/
# Solution:

from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            j = 0
            for char in query:
                if j < len(pattern) and char == pattern[j]:
                    j += 1
                elif char.isupper():
                    return False
            return j == len(pattern)
            
        return [match(q, pattern) for q in queries]

if __name__ == "__main__":
    solution = Solution()
    
    q1 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    p1 = "FB"
    print(f"Camelcase match {q1}, pattern {p1}: {solution.camelMatch(q1, p1)}")
