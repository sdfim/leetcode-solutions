# Print Immutable Linked List in Reverse
# Problem: https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
# Solution:

class ImmutableListNode:
    def __init__(self, val):
        self.val = val

    def printValue(self):
        print(self.val)

    def getNext(self):
        pass

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if not head:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()

if __name__ == "__main__":
    # Example use case
    # This is a placeholder example since ImmutableListNode cannot be instantiated directly.
    print("Immutable linked list printed in reverse.")
