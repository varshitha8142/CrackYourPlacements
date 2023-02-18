class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=0
        a=[]
        for i in nums:
            x+=i
            a.append(x)
        return a