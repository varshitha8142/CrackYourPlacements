class Solution:
    def reverseBits(self, n: int) -> int:
        x=''
        i=0;x1=0
        while n>=1:
            n1=n%2
            n=n//2
            x+=str(n1)
        if len(x)!=32:
            x=x+('0'*(32-len(x)))
        while i<len(x):
            x1+=int(x[-i-1])*(2**i)
            i+=1
        return x1
       
        