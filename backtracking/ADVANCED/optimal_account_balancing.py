# Optimal Account Balancing
# Problem: https://leetcode.com/problems/optimal-account-balancing/
# Solution:

from typing import List

def minTransfers(transactions: List[List[int]]) -> int:
    def dfs(index):
        while index < len(balances) and balances[index] == 0:
            index += 1
        if index == len(balances):
            return 0

        min_transfers = float("inf")
        for i in range(index + 1, len(balances)):
            if balances[i] * balances[index] < 0:
                balances[i] += balances[index]
                min_transfers = min(min_transfers, 1 + dfs(index + 1))
                balances[i] -= balances[index]
        return min_transfers

    balances = {}
    for u, v, amount in transactions:
        balances[u] = balances.get(u, 0) - amount
        balances[v] = balances.get(v, 0) + amount

    balances = list(filter(lambda x: x != 0, balances.values()))
    return dfs(0)

if __name__ == "__main__":
    transactions = [[0, 1, 10], [2, 0, 5]]
    print(minTransfers(transactions))
