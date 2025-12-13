# Pyramid Transition Matrix
# Problem: https://leetcode.com/problems/pyramid-transition-matrix/
# Solution:

from typing import List

def pyramidTransition(bottom: str, allowed: List[str]) -> bool:
    def backtrack(current):
        if len(current) == 1:
            return True

        next_level = []
        for i in range(len(current) - 1):
            pair = current[i:i + 2]
            if pair not in transitions:
                return False
            next_level.append(transitions[pair])

        def build_next_level(index, path):
            if index == len(next_level):
                return backtrack(path)

            for char in next_level[index]:
                if build_next_level(index + 1, path + char):
                    return True
            return False

        return build_next_level(0, "")

    transitions = {}
    for triplet in allowed:
        if triplet[:2] not in transitions:
            transitions[triplet[:2]] = []
        transitions[triplet[:2]].append(triplet[2])

    return backtrack(bottom)

if __name__ == "__main__":
    bottom = "BCD"
    allowed = ["BCG", "CDE", "GEA", "FFF"]
    print(pyramidTransition(bottom, allowed))
