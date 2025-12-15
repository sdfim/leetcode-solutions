# Backspace String Compare
# Problem: https://leetcode.com/problems/backspace-string-compare/
# Solution:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_valid_char_idx(str_val, index):
            backspace_count = 0
            while index >= 0:
                if str_val[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index
        
        i, j = len(s) - 1, len(t) - 1
        
        while i >= 0 or j >= 0:
            i = get_valid_char_idx(s, i)
            j = get_valid_char_idx(t, j)
            
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                return False
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
            
        return True

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "ab#c"
    t1 = "ad#c"
    print(f"'{s1}' == '{t1}': {solution.backspaceCompare(s1, t1)}")
    
    s2 = "ab##"
    t2 = "c#d#"
    print(f"'{s2}' == '{t2}': {solution.backspaceCompare(s2, t2)}")
    
    s3 = "a#c"
    t3 = "b"
    print(f"'{s3}' == '{t3}': {solution.backspaceCompare(s3, t3)}")
