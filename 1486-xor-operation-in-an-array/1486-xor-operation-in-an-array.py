class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a=0
        while (n>=1):
            a^=start
            start+=2
            n-=1
        return a
        