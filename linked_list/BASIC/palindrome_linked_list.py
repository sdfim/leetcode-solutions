# Palindrome Linked List
# Problem: https://leetcode.com/problems/palindrome-linked-list/
# Solution:

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True

if __name__ == "__main__":
    # Example use case
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    linked_list = create_linked_list([1, 2, 2, 1])
    solution = Solution()
    print("Is Palindrome:", solution.isPalindrome(linked_list))
