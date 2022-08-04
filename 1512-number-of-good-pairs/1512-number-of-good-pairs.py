class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x=[]
        a=list(set(nums))
        for i in range(len(a)):
            a1=nums.count(a[i])-1
            b=(a1*(a1+1))//2
            x.append(b)
        return sum(x)