class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a=0
        c=1
        while (c<=n):
            a^=start
            start+=2
            c+=1
        return a
        