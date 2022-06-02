class Solution:
    def countPrimes(self, n: int) -> int:
        a=[0,0]+[1]*(n-2)
        for i in range(2,(int(n**0.5))+1):
            if(a[i]==1):
                a[i**2::i]=[0]*len(a[i**2::i])
        return sum(a)
        