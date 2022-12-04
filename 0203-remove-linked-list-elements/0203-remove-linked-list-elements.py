# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        fast=dummy_head
        while fast.next:
            if fast.next.val==val:
                fast.next=fast.next.next
            else:
                fast=fast.next
        return dummy_head.next
        
        