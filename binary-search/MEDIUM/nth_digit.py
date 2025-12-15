# Nth Digit
# Problem: https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1-9: 9 digits
        # 10-99: 90 * 2 = 180 digits
        # 100-999: 900 * 3 = 2700 digits
        
        length = 1
        count = 9
        
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            
        start_num = 10 ** (length - 1)
        # Find the number
        num = start_num + (n - 1) // length
        # Find the digit inside the number
        idx = (n - 1) % length
        
        return int(str(num)[idx])

if __name__ == "__main__":
    solution = Solution()
    print(solution.findNthDigit(11))  # Output: 0
    print(solution.findNthDigit(3))   # Output: 3
