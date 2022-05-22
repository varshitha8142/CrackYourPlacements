class Solution:
    def maxDepth(self, s: str) -> int:
        a=s
        x=[]
        res=0
        for i in range(len(a)):
            if '('==a[i] :
                x.append(a[i])
                res = max(res, len(x))
            elif ')'==a[i]:
                x.pop()
        return res
