# Reach a Number
# Problem: https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        s = 0
        while s < target:
            k += 1
            s += k
            
        dist = s - target
        if dist % 2 == 0:
            return k
        else:
            if (k + 1) % 2 == 1: # (k+1) is odd, so dist + (k+1) is odd + odd = even
                return k + 1
            else:
                return k + 2

if __name__ == "__main__":
    solution = Solution()
    print(solution.reachNumber(3))  # Output: 2
    print(solution.reachNumber(2))  # Output: 3
