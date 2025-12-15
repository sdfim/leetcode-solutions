# Bag of Tokens
# Problem: https://leetcode.com/problems/bag-of-tokens/
# Solution:

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        max_score = 0
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
                
        return max_score

if __name__ == "__main__":
    solution = Solution()
    
    t1 = [100]
    p1 = 50
    print(f"Score tokens={t1}, power={p1}: {solution.bagOfTokensScore(t1, p1)}")
    
    t2 = [100,200,300,400]
    p2 = 200
    print(f"Score tokens={t2}, power={p2}: {solution.bagOfTokensScore(t2, p2)}")
