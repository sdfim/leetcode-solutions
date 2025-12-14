# Delete Nodes From Linked List Present in Array
# Problem: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Solution:

from typing import Optional, List
from linked_list.utils import ListNode, create_linked_list, print_linked_list

class Solution:
    def deleteNodes(self, head: Optional[ListNode], nums: List[int]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

if __name__ == "__main__":
    # Example use case
    head = create_linked_list([1, 2, 3, 4, 5])
    nums = [2, 4]
    solution = Solution()
    result = solution.deleteNodes(head, nums)
    print("Deleted nodes present in array:")
    print_linked_list(result)
