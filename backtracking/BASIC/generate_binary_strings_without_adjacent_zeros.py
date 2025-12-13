# Generate Binary Strings Without Adjacent Zeros
# Problem: Custom Problem
# Solution:

def generateBinaryStrings(n: int) -> list:
    def backtrack(index, path):
        if index == n:
            result.append("".join(path))
            return

        path.append("1")
        backtrack(index + 1, path)
        path.pop()

        if not path or path[-1] != "0":
            path.append("0")
            backtrack(index + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    n = 3
    print(generateBinaryStrings(n))
