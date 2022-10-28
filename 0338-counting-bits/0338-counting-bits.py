class Solution:
    def countBits(self, n: int) -> List[int]:
        x=[]
        for i in range(0,n+1):
            i=bin(i).replace('0b','')
            x.append(i.count('1'))
        return x