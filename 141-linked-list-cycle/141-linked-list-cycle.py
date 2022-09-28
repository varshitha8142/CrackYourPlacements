# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c=head
        a=set()
        while c:
            if c in a:
                return c
            a.add(c)
            c=c.next
        return None
        