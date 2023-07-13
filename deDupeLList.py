# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1: image[list1]


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2: image[list2]


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cmpHolder = head
        if not cmpHolder:
            return head
        cmpTarget = cmpHolder.next
        while cmpTarget:
            if not cmpTarget.val == cmpHolder.val:
                cmpHolder.next = cmpTarget
                cmpHolder = cmpTarget
            cmpTarget = cmpTarget.next
        cmpHolder.next = None
        return head
        