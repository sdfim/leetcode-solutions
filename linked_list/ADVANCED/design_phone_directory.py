# Design Phone Directory
# Problem: https://leetcode.com/problems/design-phone-directory/
# Solution:

class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))
        self.in_use = set()

    def get(self) -> int:
        if not self.available:
            return -1
        number = self.available.pop()
        self.in_use.add(number)
        return number

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        if number in self.in_use:
            self.in_use.remove(number)
            self.available.add(number)

if __name__ == "__main__":
    # Example use case
    directory = PhoneDirectory(3)
    print(directory.get())  # 0
    print(directory.get())  # 1
    print(directory.check(2))  # True
    print(directory.get())  # 2
    print(directory.check(2))  # False
    directory.release(2)
    print(directory.check(2))  # True
