# Split a String Into the Max Number of Unique Substrings
# Problem: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
# Solution:

def maxUniqueSplit(s: str) -> int:
    def backtrack(start, seen):
        if start == len(s):
            return len(seen)
        max_count = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                max_count = max(max_count, backtrack(end, seen))
                seen.remove(substring)
        return max_count

    return backtrack(0, set())

if __name__ == "__main__":
    s = "ababccc"
    print(maxUniqueSplit(s))
