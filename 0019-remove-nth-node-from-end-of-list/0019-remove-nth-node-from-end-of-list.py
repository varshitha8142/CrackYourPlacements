# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0;i=0
        slow=head
        fast=head
        while slow:
            c+=1
            slow=slow.next
        a=(c-n)
        if a==0:
            temp = head
            head = head.next
            temp = None
            return head
        while i<a:
            i+=1
            if i==a:
                fast.next=fast.next.next
                return head
            fast=fast.next
            
                