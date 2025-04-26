# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointer for the previous node (starts as None)
        prev_node: Optional[ListNode] = None
        # Initialize pointer for the current node (starts at the original head)
        current_node: Optional[ListNode] = head

        # Iterate while there's a current node to process
        while current_node is not None:
            # 1. Store the next node *before* changing the pointer
            next_temp = current_node.next

            # 2. Reverse the pointer of the current node
            #    It should now point to the node that came before it (prev_node)
            current_node.next = prev_node

            # 3. Move the pointers one step forward for the next iteration
            #    The current node becomes the previous node for the next step
            prev_node = current_node
            #    The stored next node becomes the current node for the next step
            current_node = next_temp

        # When the loop finishes, current_node is None, and prev_node
        # points to the last node of the original list, which is the
        # new head of the reversed list.
        return prev_node

        
