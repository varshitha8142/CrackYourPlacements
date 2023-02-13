class Solution:
    from itertools import permutations 
    def getPermutation(self, n: int, k: int) -> str:
        a=list(range(1,n+1))
        x=[]
        b=permutations(a)
        for i in b:
            x.append(i)
        return ''.join([str(i) for i in x[k-1]])
        