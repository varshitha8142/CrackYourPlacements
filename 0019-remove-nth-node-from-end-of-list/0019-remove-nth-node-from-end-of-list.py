# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0;d=0
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
        while fast:
            d+=1
            if d==a:
                fast.next=fast.next.next
            else:
                fast=fast.next
        return head
                