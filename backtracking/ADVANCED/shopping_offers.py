# Shopping Offers
# Problem: https://leetcode.com/problems/shopping-offers/
# Solution:

from typing import List

def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def dfs(needs):
        if tuple(needs) in memo:
            return memo[tuple(needs)]

        cost = sum(need * p for need, p in zip(needs, price))
        for offer in special:
            new_needs = [needs[i] - offer[i] for i in range(len(needs))]
            if all(n >= 0 for n in new_needs):
                cost = min(cost, offer[-1] + dfs(new_needs))

        memo[tuple(needs)] = cost
        return cost

    memo = {}
    return dfs(needs)

if __name__ == "__main__":
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    print(shoppingOffers(price, special, needs))
