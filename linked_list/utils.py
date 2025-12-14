# Utility functions for linked list operations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """
    Create a linked list from a list of values.

    Args:
        values (list): List of values to create the linked list.

    Returns:
        ListNode: Head of the created linked list.
    """
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """
    Print the linked list in a readable format.

    Args:
        head (ListNode): Head of the linked list.
    """
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))
