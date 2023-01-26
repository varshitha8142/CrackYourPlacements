class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=[];x1=[]
        for i in set(nums):
            x.append(nums.count(i))
            x1.append(i)
        a=x.index(max(x))
        return(x1[a])


