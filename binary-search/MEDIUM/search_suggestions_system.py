# Search Suggestions System
# Problem: https://leetcode.com/problems/search-suggestions-system/

from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        
        # We can maintain the range of valid products
        start, end = 0, len(products) - 1
        
        for i, char in enumerate(searchWord):
            prefix += char
            
            # Move start to the first word >= prefix
            idx = bisect.bisect_left(products, prefix, lo=start, hi=end+1)
            start = idx
            
            # We don't necessarily update end strictly with bisect, 
            # we just take up to 3 valid ones starting from start
            
            suggest = []
            for j in range(start, min(start + 3, len(products))):
                if products[j].startswith(prefix):
                    suggest.append(products[j])
                    
            res.append(suggest)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
