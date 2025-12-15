# Maximize the Confusion of an Exam
# Problem: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        
        def solve(target_char):
            # Sliding window to find max length with at most k updates to match target_char
            # i.e., at most k characters that are NOT target_char
            left = 0
            count_other = 0
            res = 0
            
            for right in range(n):
                if answerKey[right] != target_char:
                    count_other += 1
                
                while count_other > k:
                    if answerKey[left] != target_char:
                        count_other -= 1
                    left += 1
                    
                res = max(res, right - left + 1)
            return res
            
        return max(solve('T'), solve('F'))

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxConsecutiveAnswers("TTFF", 2)) # 4
