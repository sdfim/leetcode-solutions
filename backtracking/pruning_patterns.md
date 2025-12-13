# Pruning Patterns in Backtracking

## 1. Sorting + skip duplicates
Used in:
- Combination Sum II
- Subsets II
- Permutations II

Rule:
if i > start and nums[i] == nums[i - 1]:
continue

---

## 2. Early termination
Used in:
- Combination Sum
- K-partition problems

Example:
if current_sum > target:
return

---

## 3. Bitmask pruning
Used in:
- Stickers to Spell Word
- Campus Bikes II
- Maximum Score After N Operations

---

## 4. Symmetry breaking
Used in:
- N-Queens
- Partition problems

Example:
Only try empty bucket once.

---

## 5. Memoization on state
Used in:
- Word Break II
- Flip Game II
- Stickers to Spell Word
