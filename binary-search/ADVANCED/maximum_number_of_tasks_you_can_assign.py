# Maximum Number of Tasks You Can Assign
# Problem: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

from typing import List
import collections

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n = len(tasks)
        m = len(workers)
        
        def check(k):
            # Can we complete the k smallest tasks using the k strongest workers?
            if k == 0: return True
            
            current_tasks = tasks[:k]
            current_workers = workers[-k:] # k strongest workers
            
            # We want to match tasks to workers.
            # Greedy: Pick largest task. Try to assign to strongest worker without pill.
            # If not possible, try with pill.
            # Actually: Iterate tasks from Largest to Smallest.
            # Trying to assign largest task constraint is hardest.
            
            dq = collections.deque(current_workers)
            # Efficient structure?
            # We need to remove elements.
            # Using deque is tricky if we remove from middle.
            # Valid greedy strategy:
            # Process tasks from largest to smallest.
            # For current task T:
            # 1. Try largest worker W_max. If W_max >= T, use him (no pill).
            #    We should save pill for later?
            #    Actually, keeping strongest worker for harder tasks?
            #    Wait, current task T is the HARDEST among remaining.
            #    If W_max can do it without pill, great.
            #    Does using W_max without pill hurt?
            #    Maybe W_max could do T_prev without pill, but W_next needs pill for T_prev?
            #    Correct greedy: Process tasks largest to smallest.
            #    Check strongest worker W.
            #    If W >= T: great, use him (he is overkill maybe, but capable).
            #    If W < T: we MUST use a pill.
            #    Who should take the pill? Strongest worker? Or Weakest possible worker who becomes >= T?
            #    If we use strongest worker + pill, he becomes W + strength.
            #    If W + str < T, impossible.
            #    If valid, we use him.
            
            # Better Greedy:
            # Match smallest task? No.
            # Correct Greedy from solutions:
            # Use Multiset/Deque of workers.
            # Iterate k tasks from largest to smallest.
            # For task T:
            #   If strongest worker w_max >= T:
            #      Assign w_max to T?
            #      Actually we should use the WEAKEST valid worker? No.
            #      Standard logic: Use deque of available workers.
            #      But workers are fixed.
            
            # Let's use sorted list of workers.
            # Iterate tasks LARGE -> SMALL.
            # 1. Can strongest worker do it?
            #    If yes, we want to save strongest worker for an even harder task?
            #    No, T is the hardest current.
            #    So if W_max can do T, should we use him?
            #    Maybe W_mid can also do T?
            #    If W_mid can do T, and we use W_max, we waste strength.
            #    So we should use the *weakest* worker who can do T?
            #    But if we need pills?
            
            # Correct greedy with Deque:
            # Use `k` strongest workers.
            # Iterate tasks from Smallest to Largest? No.
            # Iterate tasks Largest to Smallest.
            # Keep available workers in a sorted structure (or map).
            # But deque allows removal from ends.
            
            # Actually: process tasks Smallest to Largest?
            # Let's stick to the common approach:
            # Check(k) uses `workers[-k:]`.
            # Use a deque of workers.
            # Iterate tasks from largest to smallest?
            # No.
            # Let's iterate tasks from `k-1` down to 0 (Largest subset task).
            # Try to satisfy task `tasks[i]`.
            # If `workers[-1] >= tasks[i]`:
            #    We can satisfy task. Which worker to use?
            #    We should use the strongest worker? Or weakest valid?
            #    Wait, standard solution uses deque.
            #    Process tasks smallest to largest? No.
            
            # Standard accepted strategy:
            # Tasks: T1 <= T2 <= ... <= Tk.
            # Workers: W1 <= W2 <= ... <= Wk.
            # Iterate tasks from Tk down to T1. (Hardest to Easiest).
            # 1. If W(strongest) >= T:
            #    We use W(strongest). (Matches easiest logic? No.)
            #    Actually, if W_strong >= T, he satisfies it.
            #    Does using him hurt? Maybe he was needed for T+1? No, T is max.
            #    Ok, use him.
            # 2. If W(strongest) < T:
            #    We MUST use pill.
            #    Use pill on W(strongest)?
            #    If W(strongest) + S < T: Impossible, return False.
            #    Else: Use pill. Which worker to use?
            #    We should use the WEAKEST worker such that W + S >= T.
            #    This saves stronger workers for other tasks (maybe without pill).
            
            # To implementing "Weakest w with pill":
            # We need efficient lookup/removal.
            # `current_workers` is sorted list.
            # Python list `pop(index)` is O(k). Total O(k^2).
            # Constraints: N, M <= 5*10^4. O(k^2) check is too slow inside BS.
            # We need O(k log k) or O(k).
            # Use `deque` optimization?
            # Yes. `deque` allows popping from ends.
            # Can we maintain invariant?
            
            # Optimization:
            # Use Deque of workers.
            # Iterate tasks `i` from `k-1` down to `0`.
            # But we need to search "Weakest worker + pill >= T".
            # This requires searching in middle.
            # Deque doesn't support middle removal efficiently.
            
            # Alternate Check(k):
            # Iterate tasks from Smallest to Largest.
            # Maintain a pool of workers who can satisfy current task (maybe with pill?).
            # This is hard.
            
            # Revisit "Weakest worker + pill >= T".
            # Can we use `SortedList`? Python doesn't have it.
            # But notice we iterate tasks in order.
            # Maybe we can use the fact `workers` is sorted.
            
            # Valid Greedy:
            # Use `workers[-k:]`.
            # Iterate tasks from `k-1` down to 0. (Hardest tasks first).
            # Use a deque for workers.
            # But effectively we need to pick from sorted list.
            # Trick:
            # We iterate tasks T from largest.
            # If `workers[-1] >= T`:
            #   Use `workers.pop()`. (Max worker).
            # Else:
            #   Need pill. Count pills.
            #   Find smallest W in `workers` such that `W + S >= T`.
            #   Remove that W.
            #   This middle removal is vital.
            
            # Is O(K^2) acceptable?
            # N = 50,000. No.
            
            # Is there O(N) check?
            # Use a deque `q`.
            # Workers sorted.
            # For each task `T`, we identify eligible workers.
            pass
            
            # Official O(N) check:
            # Use deque.
            # Iterate `task` in sorted `tasks[:k]`. (Smallest to Largest).
            # For `task`, add all workers `w` such that `w + strength >= task` to deque?
            # No, `w + strength`. Pill logic.
            
            # Let's use the property:
            # Iterate tasks from Largest (`k-1`) to Smallest (`0`).
            # Workers available: `ws = workers[-k:]`.
            # Use a deque `dq` to store workers.
            # Actually, `workers` are sorted.
            # But we need to pick "Weakest valid with pill".
            # Wait, `bisect` logic inside check?
            # Still removal is problem.
            
            # Let's use the Queue approach correctly:
            # Check(k):
            #   ws = workers[-k:]
            #   dq = deque()
            #   p = pills_available
            #   curr_worker_idx = k - 1
            #   
            #   Iterate tasks `i` from `k-1` down to `0` (Largest to Smallest).
            #   BUT we want to match tasks to workers.
            #   
            #   Correct logic:
            #   Iterate tasks from Smallest to Largest? Or Largest to Smallest?
            #   Let's check a known O(N) strategy.
            #   
            #   Iterate tasks from `k-1` down to `0`. (Largest T).
            #   While `curr_worker_idx >= 0` and `ws[curr_worker_idx] + strength >= T`:
            #       dq.appendleft(ws[curr_worker_idx])
            #       curr_worker_idx -= 1
            #   
            #   (dq contains workers who can do T with pill. Ordered largest to smallest).
            #   
            #   We want to match T.
            #   Option 1: Use strong worker without pill? 
            #     Worker max is `dq[0]`.
            #     If `dq[0] >= T`:
            #         We prefer to use him without pill.
            #         But saving him might be useful?
            #         Actually, if we use him, we use the strongest available.
            #         Is it better to use "Weakest who can do without pill"?
            #         All in `dq` need pill? No, `dq` has everyone `w + S >= T`.
            #         Some might have `w >= T`.
            #         Those w >= T are at the left of dq (since ws sorted increasing, we scan backwards).
            #         
            #   Refined:
            #   dq stores workers[i] such that `workers[i] + strength >= current_task`.
            #   From largest worker downwards.
            #   
            #   For task T:
            #       Add eligible workers (w + S >= T) to dq.
            #       Worker w is eligible if w + S >= T.
            #   
            #   Try to use strongest worker (dq[0]) WITHOUT pill.
            #   If dq[0] >= T:
            #       Can do without pill. Use him. Popleft.
            #   Else:
            #       Cannot do without pill (all in dq < T, even strongest).
            #       Must use pill.
            #       Use pill on WHOM?
            #       We should use the WEAKEST worker in dq (dq[-1]) to save stronger ones.
            #       Since all in dq satisfy `w + S >= T`, the weakest also satisfies with pill.
            #       Use pill. Pop right (weakest).
            #       pills -= 1. If pills < 0 return False.
            
            ws = workers[-k:]
            dq = collections.deque()
            p = pills
            w_idx = k - 1
            
            for i in range(k - 1, -1, -1):
                t = current_tasks[i]
                
                # Add workers who can potentially satisfy T with pill
                # Since T decreases, more workers become eligible.
                # But we iterate tasks largest to smallest.
                # So T decreases. `w + S >= T` becomes easier.
                # We move w_idx leftwards?
                # Wait, if T decreases, `T` is smaller.
                # `ws` are sorted smallest to largest.
                # `ws[-1]` is largest.
                # We check from largest worker.
                
                while w_idx >= 0 and ws[w_idx] + strength >= t:
                    dq.append(ws[w_idx]) # Append largest first?
                    # We iterate w_idx from k-1 down to 0.
                    # So we append Largest, then 2nd Largest...
                    # dq: [Largest, 2nd Largest ... Weakest_Eligible]
                    w_idx -= 1
                    
                if not dq:
                    return False
                
                # Try strongest (dq[0]) without pill
                if dq[0] >= t:
                    dq.popleft()
                else:
                    # Use pill on weakest available (dq[-1])
                    if p > 0:
                        p -= 1
                        dq.pop()
                    else:
                        return False
            return True

        left, right = 0, min(n, m)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTaskAssign([3,2,1], [0,3,3], 1, 1)) # Output: 3
