# Partition to K Equal Sum Subsets
from typing import List
def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    # Solution:
    # Problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

    def backtrack(index, current_sum, count):
        if count == k:
            return True
        if current_sum == target:
            return backtrack(0, 0, count + 1)
        for i in range(index, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if backtrack(i + 1, current_sum + nums[i], count):
                    return True
                used[i] = False
        return False

    nums.sort(reverse=True)
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    used = [False] * len(nums)
    return backtrack(0, 0, 0)

if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(canPartitionKSubsets(nums, k))
