# Comparison Version Numbers
# Problem: https://leetcode.com/problems/compare-version-numbers/
# Solution:

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n, m = len(v1), len(v2)
        
        i = 0
        while i < n or i < m:
            val1 = int(v1[i]) if i < n else 0
            val2 = int(v2[i]) if i < m else 0
            
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
            i += 1
            
        return 0

if __name__ == "__main__":
    solution = Solution()
    
    v1 = "1.01"
    v2 = "1.001"
    print(f"Compare {v1}, {v2}: {solution.compareVersion(v1, v2)}")
    
    v1 = "1.0"
    v2 = "1.0.0"
    print(f"Compare {v1}, {v2}: {solution.compareVersion(v1, v2)}")
    
    v1 = "0.1"
    v2 = "1.1"
    print(f"Compare {v1}, {v2}: {solution.compareVersion(v1, v2)}")
