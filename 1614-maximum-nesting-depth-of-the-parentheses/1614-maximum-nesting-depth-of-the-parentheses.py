class Solution:
    def maxDepth(self, s: str) -> int:
        a=s
        x=[]
        z=[]
        res=0
        for i in range(len(a)):
            if '('==a[i] :
                x.append(a[i])
                z.append(len(x))
            elif ')'==a[i]:
                x.pop()
        z.sort()
        if len(z)>1:
            return z[-1]
        return len(z)
