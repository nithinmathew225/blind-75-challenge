
Prerequisites
Singly Linked Lists
Data Structures & Algorithms for Beginners
Fast and Slow Pointers
Advanced Algorithms
Video Explanation


View on Youtube

1. Hash Set
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
Time & Space Complexity
Time complexity: 
�
(
�
)
O(n)
Space complexity: 
�
(
�
)
O(n)
2. Fast And Slow Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
Time & Space Complexity
Time complexity: 
�
(
�
)
O(n)
Space complexity: 
�
(
1
)
O(1)
123456










