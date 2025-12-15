# Longest Uploaded Prefix
# Problem: https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix:

    def __init__(self, n: int):
        self.uploaded = set()
        self.longest = 0

    def upload(self, video: int) -> None:
        self.uploaded.add(video)
        while self.longest + 1 in self.uploaded:
            self.longest += 1

    def longest(self) -> int:
        return self.longest

# Note output method name conflict in python if property has same name.
# LeetCode method is 'longest()', class has 'longest' var.
# Renamed method in Python usually fine or field different name.
# I'll use `max_prefix` for field.

class LUPrefixClean:
    def __init__(self, n: int):
        self.uploaded = set()
        self.max_prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded.add(video)
        while self.max_prefix + 1 in self.uploaded:
            self.max_prefix += 1

    def longest(self) -> int:
        return self.max_prefix

if __name__ == "__main__":
    obj = LUPrefixClean(4)
    obj.upload(3)
    print(obj.longest()) # 0
    obj.upload(1)
    print(obj.longest()) # 1
    obj.upload(2)
    print(obj.longest()) # 3
