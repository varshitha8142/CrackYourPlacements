class Solution:
    def reverseBits(self, n: int) -> int:
        n=(str(bin(n))[::-1]).replace('b0','')
        if len(n)!=32:
            n=n+('0'*(32-len(n)))
        return (int(n,2))
        
       
        