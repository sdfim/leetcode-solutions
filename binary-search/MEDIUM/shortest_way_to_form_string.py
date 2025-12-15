# Shortest Way to Form String
# Problem: https://leetcode.com/problems/shortest-way-to-form-string/

import collections

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Precompute indices of each char in source
        # or use next_occurrence array.
        
        n = len(source)
        # next_occ[i][char] = index of first occurrence of char at or after i
        
        # Optimization: Just inverted index
        char_indices = collections.defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)
            
        import bisect
        
        count = 1
        current_idx = -1
        
        for char in target:
            if char not in char_indices:
                return -1
                
            indices = char_indices[char]
            
            # Find smallest index in indices that is > current_idx
            idx = bisect.bisect_right(indices, current_idx)
            
            if idx == len(indices):
                # Need new subsequence
                count += 1
                current_idx = -1
                idx = bisect.bisect_right(indices, current_idx)
                # Must extend. Since char exists, idx will be valid (at least 0)
                current_idx = indices[idx]
            else:
                current_idx = indices[idx]
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestWay("abc", "abcbc")) # 2
