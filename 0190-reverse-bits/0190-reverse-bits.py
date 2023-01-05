class Solution:
    def reverseBits(self, n: int) -> int:
        x=''
        i=0
        while (n>=1):
            n1=n%2
            n=n//2
            x+=str(n1)
        if len(x)!=32:
            x=x+('0'*(32-len(x)))
        return (int(x,2))
        
       
        