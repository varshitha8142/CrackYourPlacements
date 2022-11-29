# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        slow,fast,prev=head,head,head
        if head.next==None:
            return 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            c+=1
            if c>1:
                prev=prev.next
        prev.next=slow.next
        return head
        