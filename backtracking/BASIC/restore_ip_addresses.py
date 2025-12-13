# Restore IP Addresses
# Problem: https://leetcode.com/problems/restore-ip-addresses/
# Solution:

from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(end, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    s = "25525511135"
    print(restoreIpAddresses(s))
