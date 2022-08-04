class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=nums
        d={}
        c=0
        for i in range(len(a)):
            if a[i] in d:
                d[a[i]]+=1
                c+=d[a[i]]
            else:
                d[a[i]]=0
        return c