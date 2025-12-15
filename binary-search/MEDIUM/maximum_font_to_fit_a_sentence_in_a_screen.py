# Maximum Font to Fit a Sentence in a Screen
# Problem: https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

from typing import List

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
class FontInfo(object):
    def getWidth(self, fontSize: int, ch: str) -> int:
        pass
    def getHeight(self, fontSize: int) -> int:
        pass

class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        def can(size):
            # Check height
            height = fontInfo.getHeight(size)
            if height > h:
                return False
                
            # Check width
            # Naive: sum widths. If multiline allowed, more complex.
            # Problem description implies: "single line" usually?
            # Or "fit a sentence in a screen" often implies multiline wrap.
            # But the FontInfo API suggests getting char width.
            # Let's assume standard problem where we just check summing widths vs w (if single line default).
            # "Maximum Font to Fit a Sentence in a Screen" -> usually implies multiline wrap logic IS NOT trivial 
            # OR typically simple check total width if 1 line.
            # Actually, standard problem usually asks if lines fit.
            # Without detailed text, let's assume simple width capacity check since "Screen" usually implies W x H.
            # If multiline, we need to wrap words.
            # Assume naive implementation: all in one line or wrapping?
            # Usually: If total width of chars > w, fail? Or check wrapping.
            # Given typically constraint: we check if sum of widths <= w?
            # NO: LeetCode 1618 is distinct.
            
            # Let's check typical constraints for 1618:
            # We must fit ALL characters.
            # If total sum > w?
            # It seems we check if the entire text fits on the screen width w?
            # Or if it can wrap within height h? "Fit text on valid lines".
            # Usually we iterate chars. Line by line.
            # But usually 1618 requires simply checking total width <= w? NO.
            # Let's implement robust wrap check if possible, or assume simple width check.
            
            # Re-reading similar problems: "Sentence Screen Fitting" is 418. "Maximum font" is 1618.
            # 1618 logic: 
            # 1. Height of one line must be <= h. (Usually only 1 line fits? Or multiple?)
            # Actually, fonts only affect size.
            
            # Safety check: if standard check fails, we return False.
            
            total_w = 0
            for ch in text:
                total_w += fontInfo.getWidth(size, ch)
                
            # If total width exceeds W, can we wrap?
            # If problem is "Single line text", return total_w <= w.
            # If multiline, we need to check lines.
            
            # Looking at similar LC solutions: 1618 is straightforward.
            # You are given W and H. Can fit ONLY if total width <= W and height <= H?
            # Oh, if it allows multiline, logic is harder.
            # Let's assume standard: Single Line fit unless specified.
            # Many "Maximum Font" problems assume fitting into a rectangle.
            # Let's assume we simply check:
            # for char: total_w += w(char). if total_w > w: return False.
            # if h(size) > h: return False.
            
            if fontInfo.getHeight(size) > h: 
                return False
                
            curr_w = 0
            for c in text:
                curr_w += fontInfo.getWidth(size, c)
            
            return curr_w <= w

        l, r = 0, len(fonts) - 1
        res = -1
        
        while l <= r:
            mid = (l + r) // 2
            if can(fonts[mid]):
                res = fonts[mid]
                l = mid + 1
            else:
                r = mid - 1
        return res

if __name__ == "__main__":
    # Mock
    pass
