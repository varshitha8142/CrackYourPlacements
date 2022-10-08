class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=list(range(1,n+1))
        while(len(a)>1):
            b=(k-1)%len(a)
            a.pop(b)
            a=a[b:]+a[:b]
        return a[0]
        