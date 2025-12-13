# 24 Game
# Problem: https://leetcode.com/problems/24-game/
# Solution:

from typing import List

def judgePoint24(cards: List[int]) -> bool:
    def backtrack(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    for op in {"+", "-", "*", "/"}:
                        if op == "+":
                            next_nums.append(nums[i] + nums[j])
                        elif op == "-":
                            next_nums.append(nums[i] - nums[j])
                        elif op == "*":
                            next_nums.append(nums[i] * nums[j])
                        elif op == "/" and nums[j] != 0:
                            next_nums.append(nums[i] / nums[j])

                        if backtrack(next_nums):
                            return True

                        next_nums.pop()
        return False

    return backtrack(cards)

if __name__ == "__main__":
    cards = [4, 1, 8, 7]
    print(judgePoint24(cards))
