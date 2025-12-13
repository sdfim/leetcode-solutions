from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                # skip duplicates on the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])
        return res

if __name__ == "__main__":
    nums = [1, 2, 2]
    solution = Solution()
    print(solution.subsetsWithDup(nums))
