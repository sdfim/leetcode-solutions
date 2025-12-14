# Combination Sum
# Problem: https://leetcode.com/problems/combination-sum/
# Solution:

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(remaining, start, path):
        if remaining == 0:
            result.append(list(path))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(remaining - candidates[i], i, path)
            path.pop()

    result = []
    backtrack(target, 0, [])
    return result

if __name__ == "__main__":

    # Helper function to print results clearly
    def run_test_case(case_num, candidates, target, expected):
        actual = combinationSum(candidates, target)
        # Note: Since the order of combinations might vary,
        # comparing sorted lists of sorted combinations is often required in formal tests.
        # For simple printing, we show the raw output.
        print(f"\n--- Test Case {case_num} ---")
        print(f"Input: candidates={candidates}, target={target}")
        print(f"Expected Result: {expected}")
        print(f"Actual Result:   {actual}")

    # --- Test Case 1: Basic Example (from your file) ---
    candidates_1 = [2, 3, 6, 7]
    target_1 = 7
    expected_1 = [[2, 2, 3], [7]]
    run_test_case(1, candidates_1, target_1, expected_1)

    # --- Test Case 2: Larger Target, More Combinations ---
    candidates_2 = [2, 3, 5]
    target_2 = 8
    expected_2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    run_test_case(2, candidates_2, target_2, expected_2)

    # --- Test Case 3: No Solution Possible ---
    candidates_3 = [4, 6]
    target_3 = 7
    expected_3 = []
    run_test_case(3, candidates_3, target_3, expected_3)

    # --- Test Case 4: Target equals a single candidate ---
    candidates_4 = [5, 10, 15]
    target_4 = 10
    expected_4 = [[10], [5, 5]]
    run_test_case(4, candidates_4, target_4, expected_4)
