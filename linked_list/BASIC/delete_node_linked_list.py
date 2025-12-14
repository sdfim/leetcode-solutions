from linked_list.utils import ListNode, create_linked_list, print_linked_list

# Problem: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Solution:

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next

if __name__ == "__main__":
    linked_list = create_linked_list([4, 5, 1, 9])
    solution = Solution()
    print("Original Linked List:")
    print_linked_list(linked_list)

    # Assuming we have a reference to the node with value 5
    node_to_delete = linked_list.next
    solution.deleteNode(node_to_delete)

    print("Linked List after Deletion:")
    print_linked_list(linked_list)
