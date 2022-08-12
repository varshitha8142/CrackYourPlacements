class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=nums
        a1=len(nums)//3
        x={}
        z=set()
        for i in a:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
            if x[i]>a1:
                z.add(i)
        return z