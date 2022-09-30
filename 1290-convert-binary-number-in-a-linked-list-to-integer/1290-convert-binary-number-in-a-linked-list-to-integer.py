# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        x=[];x1=[]
        while head:
            x.append(head.val)
            head=head.next
        n=len(x)-1
        for i in x:
            if i==1:
                x1.append(2**n)
            n-=1
        return sum(x1)
        
        