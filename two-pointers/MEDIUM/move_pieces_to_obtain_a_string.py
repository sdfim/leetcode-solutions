# Move Pieces to Obtain a String
# Problem: https://leetcode.com/problems/move-pieces-to-obtain-a-string/
# Solution:

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
            
        l_idx_s = [i for i, c in enumerate(start) if c == 'L']
        l_idx_t = [i for i, c in enumerate(target) if c == 'L']
        
        for i, j in zip(l_idx_s, l_idx_t):
            if i < j: # L can only move left
                return False
                
        r_idx_s = [i for i, c in enumerate(start) if c == 'R']
        r_idx_t = [i for i, c in enumerate(target) if c == 'R']
        
        for i, j in zip(r_idx_s, r_idx_t):
            if i > j: # R can only move right
                return False
                
        return True

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "_L__R__R_"
    t1 = "L______RR"
    print(f"Can change '{s1}' to '{t1}': {solution.canChange(s1, t1)}")
