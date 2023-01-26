class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        i=list(d.values())
        j=list(d.keys())
        a=i.index(max(i))
        return(j[a])