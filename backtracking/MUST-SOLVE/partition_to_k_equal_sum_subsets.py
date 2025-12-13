# Partition to K Equal Sum Subsets
# Problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Solution:

from typing import List

def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    target, remainder = divmod(sum(nums), k)
    if remainder != 0 or max(nums) > target:
        return False

    nums.sort(reverse=True)
    buckets = [0] * k

    def backtrack(index):
        if index == len(nums):
            return True
        for i in range(k):
            if buckets[i] + nums[index] <= target:
                buckets[i] += nums[index]
                if backtrack(index + 1):
                    return True
                buckets[i] -= nums[index]
            if buckets[i] == 0:
                break
        return False

    return backtrack(0)

if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(canPartitionKSubsets(nums, k))
