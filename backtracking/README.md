# Backtracking — LeetCode Solutions

This folder contains **all problems from the official LeetCode Backtracking list**  
(100% coverage, including latest additions).

Problems are grouped by **conceptual difficulty**, not by LeetCode labels.

## Structure

backtracking/  
├── [BASIC/](./BASIC/)  
├── [MEDIUM/](./MEDIUM/)  
├── [ADVANCED/](./ADVANCED/)  
├── [MUST-SOLVE/](./MUST-SOLVE/)  
├── [template.md](./template.md)  
└── [pruning_patterns.md](./pruning_patterns.md)

---

## 📁 BASIC
Classic backtracking problems.
Single recursive function, no complex state.

Typical patterns:
- generate all combinations / permutations
- choose → explore → unchoose
- no memoization

Examples:
- Generate Parentheses
- Permutations
- Subsets
- Combination Sum

---

## 📁 MEDIUM
Backtracking with constraints and pruning.

Typical patterns:
- deduplication
- sorting + skipping
- early stopping
- partial memoization

Examples:
- Word Search
- Target Sum
- Partition to K Equal Sum Subsets
- Palindrome Permutation II

---

## 📁 ADVANCED
Hard problems with complex state.

Typical patterns:
- bitmasking
- graph + backtracking
- DFS + DP
- strong pruning

Examples:
- Sudoku Solver
- N-Queens
- Word Search II
- Remove Invalid Parentheses
- Stickers to Spell Word

---

## ✅ Coverage

✔ 100% of problems from  
https://leetcode.com/problem-list/backtracking/

Last verified: 2025-01-15


## Categories

### 1. Basic
1. **[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)** - [Solution](./BASIC/letter_combinations.py)
2. **[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)** - [Solution](./BASIC/generate_parentheses.py)
3. **[39. Combination Sum](https://leetcode.com/problems/combination-sum/)** - [Solution](./BASIC/combination_sum.py)
4. **[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)** - [Solution](./BASIC/combination_sum_ii.py)
5. **[46. Permutations](https://leetcode.com/problems/permutations/)** - [Solution](./BASIC/permutations.py)
6. **[47. Permutations II](https://leetcode.com/problems/permutations-ii/)** - [Solution](./BASIC/permutations_ii.py)
7. **[77. Combinations](https://leetcode.com/problems/combinations/)** - [Solution](./BASIC/combinations.py)
8. **[78. Subsets](https://leetcode.com/problems/subsets/)** - [Solution](./BASIC/subsets.py)
9. **[90. Subsets II](https://leetcode.com/problems/subsets-ii/)** - [Solution](./BASIC/subsets_ii.py)
10. **[93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)** - [Solution](./BASIC/restore_ip_addresses.py)
11. **[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)** - [Solution](./BASIC/palindrome_partitioning.py)
12. **[784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)** - [Solution](./BASIC/letter_case_permutation.py)
13. **[1079. Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/)** - [Solution](./BASIC/letter_tile_possibilities.py)
14. **[1863. Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)** - [Solution](./BASIC/sum_of_all_subset_xor_totals.py)
15. **[2044. Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)** - [Solution](./BASIC/count_number_of_maximum_bitwise_or_subsets.py)
16. **[Custom. Generate Binary Strings Without Adjacent Zeros](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)** - [Solution](./BASIC/generate_binary_strings_without_adjacent_zeros.py)

### 2. Medium
1. **[79. Word Search](https://leetcode.com/problems/word-search/)** - [Solution](./MEDIUM/word_search.py)
2. **[216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)** - [Solution](./MEDIUM/combination_sum_iii.py)
3. **[254. Factor Combinations](https://leetcode.com/problems/factor-combinations/)** - [Solution](./MEDIUM/factor_combinations.py)
4. **[267. Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/)** - [Solution](./MEDIUM/palindrome_permutation_ii.py)
5. **[291. Word Pattern II](https://leetcode.com/problems/word-pattern-ii/)** - [Solution](./MEDIUM/word_pattern_ii.py)
6. **[306. Additive Number](https://leetcode.com/problems/additive-number/)** - [Solution](./MEDIUM/additive_number.py)
7. **[320. Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/)** - [Solution](./MEDIUM/generalized_abbreviation.py)
8. **[351. Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/)** - [Solution](./MEDIUM/android_unlock_patterns.py)
9. **[491. Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/)** - [Solution](./MEDIUM/non_decreasing_subsequences.py)
10. **[494. Target Sum](https://leetcode.com/problems/target-sum/)** - [Solution](./MEDIUM/target_sum.py)
11. **[526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)** - [Solution](./MEDIUM/beautiful_arrangement.py)
12. **[698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)** - [Solution](./MEDIUM/partition_to_k_equal_sum_subsets.py)
13. **[816. Ambiguous Coordinates](https://leetcode.com/problems/ambiguous-coordinates/)** - [Solution](./MEDIUM/ambiguous_coordinates.py)
14. **[842. Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)** - [Solution](./MEDIUM/split_array_into_fibonacci_sequence.py)
15. **[967. Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)** - [Solution](./MEDIUM/numbers_with_same_consecutive_differences.py)
16. **[1219. Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/)** - [Solution](./MEDIUM/path_with_maximum_gold.py)
17. **[1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)** - [Solution](./MEDIUM/maximum_length_of_a_concatenated_string_with_unique_characters.py)
18. **[1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)** - [Solution](./MEDIUM/split_a_string_into_the_max_number_of_unique_substrings.py)
19. **[2375. Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string/)** - [Solution](./MEDIUM/construct_smallest_number_from_di_string.py)
20. **[2597. The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/)** - [Solution](./MEDIUM/the_number_of_beautiful_subsets.py)

### 3. Advanced
1. **[37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)** - [Solution](./ADVANCED/sudoku_solver.py)
2. **[51. N-Queens](https://leetcode.com/problems/n-queens/)** - [Solution](./ADVANCED/n_queens.py)
3. **[52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)** - [Solution](./ADVANCED/n_queens_ii.py)
4. **[126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)** - [Solution](./ADVANCED/word_ladder_ii.py)
5. **[140. Word Break II](https://leetcode.com/problems/word-break-ii/)** - [Solution](./ADVANCED/word_break_ii.py)
6. **[212. Word Search II](https://leetcode.com/problems/word-search-ii/)** - [Solution](./ADVANCED/word_search_ii.py)
7. **[282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)** - [Solution](./ADVANCED/expression_add_operators.py)
8. **[294. Flip Game II](https://leetcode.com/problems/flip-game-ii/)** - [Solution](./ADVANCED/flip_game_ii.py)
9. **[301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)** - [Solution](./ADVANCED/remove_invalid_parentheses.py)
10. **[411. Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/)** - [Solution](./ADVANCED/minimum_unique_word_abbreviation.py)
11. **[425. Word Squares](https://leetcode.com/problems/word-squares/)** - [Solution](./ADVANCED/word_squares.py)
12. **[465. Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/)** - [Solution](./ADVANCED/optimal_account_balancing.py)
13. **[489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)** - [Solution](./ADVANCED/robot_room_cleaner.py)
14. **[638. Shopping Offers](https://leetcode.com/problems/shopping-offers/)** - [Solution](./ADVANCED/shopping_offers.py)
15. **[679. 24 Game](https://leetcode.com/problems/24-game/)** - [Solution](./ADVANCED/24_game.py)
16. **[691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/)** - [Solution](./ADVANCED/stickers_to_spell_word.py)
17. **[756. Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/)** - [Solution](./ADVANCED/pyramid_transition_matrix.py)
18. **[773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/)** - [Solution](./ADVANCED/sliding_puzzle.py)
19. **[980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)** - [Solution](./ADVANCED/unique_paths_iii.py)
20. **[996. Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/)** - [Solution](./ADVANCED/number_of_squareful_arrays.py)
21. **[1240. Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)** - [Solution](./ADVANCED/tiling_a_rectangle_with_the_fewest_squares.py)
22. **[1255. Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/)** - [Solution](./ADVANCED/maximum_score_words_formed_by_letters.py)
23. **[1307. Verbal Arithmetic Puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/)** - [Solution](./ADVANCED/verbal_arithmetic_puzzle.py)
24. **[1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/)** - [Solution](./ADVANCED/distribute_repeating_integers.py)
25. **[1718. Construct the Lexicographically Largest Valid Sequence](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/)** - [Solution](./ADVANCED/construct_the_lexicographically_largest_valid_sequence.py)
26. **[1723. Find Minimum Time to Finish All Jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)** - [Solution](./ADVANCED/find_minimum_time_to_finish_all_jobs.py)
27. **[1799. Maximize Score After N Operations](https://leetcode.com/problems/maximize-score-after-n-operations/)** - [Solution](./ADVANCED/maximize_score_after_n_operations.py)
28. **[1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)** - [Solution](./ADVANCED/minimum_number_of_work_sessions_to_finish_the_tasks.py)
29. **[2014. Longest Subsequence Repeated k Times](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)** - [Solution](./ADVANCED/longest_subsequence_repeated_k_times.py)

### 4. MUST-SOLVE

These are the top 15 must-solve problems for interviews. If you have limited time, focus on these:

1. **[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)** - [Solution](./MUST-SOLVE/generate_parentheses.py)
2. **[39. Combination Sum](https://leetcode.com/problems/combination-sum/)** - [Solution](./MUST-SOLVE/combination_sum.py)
3. **[46. Permutations](https://leetcode.com/problems/permutations/)** - [Solution](./MUST-SOLVE/permutations.py)
4. **[78. Subsets](https://leetcode.com/problems/subsets/)** - [Solution](./MUST-SOLVE/subsets.py)
5. **[79. Word Search](https://leetcode.com/problems/word-search/)** - [Solution](./MUST-SOLVE/word_search.py)
6. **[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)** - [Solution](./MUST-SOLVE/palindrome_partitioning.py)
7. **[51. N-Queens](https://leetcode.com/problems/n-queens/)** - [Solution](./MUST-SOLVE/n_queens.py)
8. **[37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)** - [Solution](./MUST-SOLVE/sudoku_solver.py)
9. **[301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)** - [Solution](./MUST-SOLVE/remove_invalid_parentheses.py)
10. **[212. Word Search II](https://leetcode.com/problems/word-search-ii/)** - [Solution](./MUST-SOLVE/word_search_ii.py)
11. **[494. Target Sum](https://leetcode.com/problems/target-sum/)** - [Solution](./MUST-SOLVE/target_sum.py)
12. **[698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)** - [Solution](./MUST-SOLVE/partition_to_k_equal_sum_subsets.py)
13. **[980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)** - [Solution](./MUST-SOLVE/unique_paths_iii.py)
14. **[691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/)** - [Solution](./MUST-SOLVE/stickers_to_spell_word.py)
15. **[140. Word Break II](https://leetcode.com/problems/word-break-ii/)** - [Solution](./MUST-SOLVE/word_break_ii.py)

---

Feel free to explore the solutions and improve your backtracking skills!
